# 🪵 Centralized Logging with the ELK Stack

A production-ready, Docker-Compose-based centralized logging pipeline.  
One command to run; logs visible in Kibana within minutes.

```
App → Filebeat → Logstash → Elasticsearch → Kibana
```

---

## 📁 Repository Structure

```
Logging-Assessment/
├── docker-compose.yml          # Entire stack
├── app/
│   ├── Dockerfile
│   └── log_generator.py        # Sample app – emits structured JSON logs
├── filebeat/
│   └── filebeat.yml            # Filebeat input + Logstash output config
├── logstash/
│   ├── config/
│   │   └── logstash.yml        # Node-level Logstash settings
│   └── pipeline/
│       └── app-logs.conf       # Input / Auto-provisions data view & dashboard
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Docker ≥ 24  
- Docker Compose plugin (`docker compose version`)  
- At least **4 GB RAM** available to Docker


### 1 — Watch the stack come up

```bash
docker compose logs -f
# Elasticsearch is ready when you see "Cluster health: green/yellow"
# Kibana is ready when you see "Server running at http://..."
# kibana-setup exits 0 once provisioning is done (~2-3 min total)
```

### 2 — Open Kibana

```
http://localhost:5601
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  Docker network: elk                                            │
│                                                                 │
│  ┌──────────────┐    /var/log/app    ┌──────────────────────┐  │
│  │ log-generator│ ──── app.log ────► │      Filebeat        │  │
│  │  (Python)    │                    │  (tail + JSON parse) │  │
│  └──────────────┘                    └──────────┬───────────┘  │
│                                                 │ :5044         │
│                                       ┌─────────▼───────────┐  │
│                                       │      Logstash        │  │
│                                       │  • date normalise    │  │
│                                       │  • severity field    │  │
│                                       │  • HTTP status tags  │  │
│                                       │  • field cleanup     │  │
│                                       └─────────┬───────────┘  │
│                                                 │ :9200         │
│                                       ┌─────────▼───────────┐  │
│                                       │   Elasticsearch      │  │
│                                       │  index: app-logs-*   │  │
│                                       └─────────┬───────────┘  │
│                                                 │               │
│                                       ┌─────────▼───────────┐  │
│                                       │       Kibana         │  │
│                                       │  :5601  (browser)    │  │
│                                       └─────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Component Roles

| Component | Role |
|-----------|------|
| **log-generator** | Python app that emits structured JSON logs with realistic service names, HTTP codes, and error payloads |
| **Filebeat** | Lightweight shipper – tails log files, parses JSON, forwards to Logstash via the Beats protocol |
| **Logstash** | Processing layer – normalises timestamps, adds `severity` integer, tags `ERROR`/`CRITICAL` events, maps HTTP status buckets |
| **Elasticsearch** | Stores all log documents in daily indices (`app-logs-YYYY.MM.dd`) |
| **Kibana** | Visualisation & exploration UI; auto-provisioned with data view and dashboard |

---

## 🔑 Key Design Decisions

### Why Filebeat + Logstash (not Filebeat → ES directly)?
Logstash gives a dedicated enrichment layer. Adding fields (like `severity`), renaming keys, and grok-parsing without touching application code is much cleaner in a Logstash pipeline than in Filebeat's limited processors.

### Why disable xpack.security for local dev?
Certificates and API keys add friction during development. In a production deployment you would enable TLS and set `ELASTIC_PASSWORD`.

### Why daily indices (`app-logs-YYYY.MM.dd`)?
Easy retention management – delete old indices with a single curator call or ILM policy. The wildcard `app-logs-*` data view covers all days automatically.

### Why structured JSON logs in the app?
Filebeat's `json.*` options ingest fields directly without regex parsing, which is both faster and more maintainable.

---

## 🔍 Using Kibana

### View all logs
1. **Analytics → Discover**
2. Select data view **App Logs** (top-left dropdown)
3. Set time range to **Last 15 minutes**

### Filter: ERROR logs only
In the KQL search bar:
```kql
level : "ERROR"
```

### Filter: a specific service
```kql
service : "payment-service"
```

### Filter: HTTP 5xx errors
```kql
tags : "http_5xx"
```

### Combined filter
```kql
level : ("ERROR" OR "CRITICAL") AND service : "api-gateway"
```

### Pre-built saved search
**Analytics → Discover → Open → "ERROR & CRITICAL Logs"**  
Shows only error-level events with columns: level, service, message, error_type.

---

## 📊 Dashboard

**Analytics → Dashboards → Application Logs Overview**

Start with the pre-provisioned dashboard skeleton, then add panels:

| Panel type | Metric |
|------------|--------|
| Metric | Total error count (`level: ERROR OR CRITICAL`) |
| Bar chart | Log volume over time (split by `level`) |
| Pie / Donut | Log distribution by `level` |
| Data table | Top 5 services by error count |
| Metric | Critical count |

**To add a panel manually:**
1. Click **Edit** on the dashboard
2. **Add panel → Create visualisation**
3. Choose Lens, set index to **app-logs-*** and drag fields

---

## 🛠️ Useful Commands

```bash
# Check Elasticsearch index
curl http://localhost:9200/_cat/indices?v

# Check document count
curl http://localhost:9200/app-logs-*/_count

# Tail raw app logs
docker compose logs -f app

# Tail Logstash output
docker compose logs -f logstash

# Restart only Filebeat (after config change)
docker compose restart filebeat

# Stop everything and clean volumes
docker compose down -v
```

---

## 🔒 Production Hardening Checklist

- [ ] Enable `xpack.security.enabled: true` and set `ELASTIC_PASSWORD`
- [ ] Configure TLS for Elasticsearch ↔ Kibana and Logstash ↔ ES
- [ ] Add an ILM (Index Lifecycle Management) policy to roll/delete old indices
- [ ] Set `ELASTIC_MEM_LIMIT` based on available RAM (≥2 GB for production)
- [ ] Store secrets in Docker secrets or a vault, not plain env vars
- [ ] Enable Filebeat monitoring to track pipeline lag

---

## 📦 Ports Summary

| Port | Service |
|------|---------|
| 9200 | Elasticsearch HTTP API |
| 5601 | Kibana UI |
| 5044 | Logstash Beats input |
| 9600 | Logstash monitoring API |

---

## 🤝 Contributing

Pull requests welcome. Please open an issue first for large changes.
