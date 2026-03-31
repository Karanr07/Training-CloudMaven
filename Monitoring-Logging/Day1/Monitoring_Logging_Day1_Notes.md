# 📊 Monitoring & Logging — Day 1 Complete Notes

> **Course:** DevOps Monitoring & Logging  
> **Topic:** Foundations of Monitoring, Logging & Observability  
> **Level:** Beginner to Intermediate

---

## 📚 Table of Contents

1. [What is Monitoring?](#1-what-is-monitoring)
2. [What is Logging?](#2-what-is-logging)
3. [Monitoring vs Logging — Key Difference](#3-monitoring-vs-logging--key-difference)
4. [Role in DevOps](#4-role-in-devops)
5. [Observability — The Big Picture](#5-observability--the-big-picture)
6. [The Three Pillars: Metrics, Logs, Traces](#6-the-three-pillars-metrics-logs-traces)
7. [Monitoring vs Logging vs Alerting](#7-monitoring-vs-logging-vs-alerting)
8. [Common Tools Overview](#8-common-tools-overview)
9. [Production-Level Tools (R&D)](#9-production-level-tools-rd)
10. [Architecture of Monitoring & Logging Stack](#10-architecture-of-monitoring--logging-stack)
11. [Linux Commands for Monitoring & Logging](#11-linux-commands-for-monitoring--logging)
12. [Best Practices](#12-best-practices)

---

## 1. What is Monitoring?

> 💡 **Simple Definition:** Monitoring is like a doctor continuously checking a patient's vitals — heartbeat, blood pressure, temperature — so they can act immediately if something goes wrong.

**Technical Definition:**  
Monitoring is the **continuous process of collecting, analyzing, and evaluating** system and application data to ensure everything is functioning correctly.

### What questions does Monitoring answer?

| Question | Example |
|----------|---------|
| Is the system up? | Server is UP / DOWN |
| Is it slow? | Response time > 2 seconds |
| Are users experiencing failures? | 500 errors spiking |
| Is resource usage abnormal? | CPU at 99% |
| Is something about to break? | Disk 95% full |

### Continuous Monitoring Capabilities

```
┌─────────────────────────────────────────────┐
│           Continuous Monitoring             │
├───────────────┬──────────────┬──────────────┤
│ Real-time     │ Proactively  │ Collect ALL  │
│ data          │ respond to   │ data across  │
│ collection    │ insights     │ systems      │
└───────────────┴──────────────┴──────────────┘
```

> 🔑 **Key Insight:** Monitoring is NOT about checking once — it's about **constant visibility**.

---

## 2. What is Logging?

> 💡 **Simple Definition:** Logs are like a diary of your system — every event, error, and action is written down with a timestamp so you can go back and read what happened.

**Technical Definition:**  
Logging is the practice of **recording discrete events** that happen within a system. Each log entry is a timestamped record of something that occurred.

### What questions does Logging answer?

| Question | Example |
|----------|---------|
| What exactly happened? | "Database connection refused" |
| When did it happen? | 2025-02-16 10:23:45 |
| Which component failed? | UserService |
| What was the error message? | `NullPointerException at line 42` |

### Example Log Entry (Structured JSON Format)

```json
{
  "timestamp": "2025-02-16T10:23:45Z",
  "level": "ERROR",
  "message": "Failed to connect to database",
  "service": "UserService",
  "userId": 42,
  "hostname": "server-1"
}
```

### Log Levels (from least to most severe)

```
DEBUG   → Detailed dev info (only during development)
INFO    → General system events (app started, user logged in)
WARN    → Something unusual but not breaking
ERROR   → Something failed but app still running
FATAL   → Critical failure, app may crash
```

---

## 3. Monitoring vs Logging — Key Difference

```
┌─────────────────────────────────────────────┐
│                 ANALOGY                     │
│                                             │
│  Monitoring = Dashboard lights in your car  │
│  (tells you the ENGINE LIGHT is ON)         │
│                                             │
│  Logging = The mechanic's diagnostic tool   │
│  (tells you WHY the engine light is ON)     │
└─────────────────────────────────────────────┘
```

> ✅ **Monitoring detects that something is WRONG.**  
> ✅ **Logging helps explain WHY it went wrong.**

---

## 4. Role in DevOps

In DevOps, development and operations teams work together to deliver applications faster and more reliably. Monitoring & Logging are critical to achieving this.

### Why Care About Monitoring?

1. **Proactive Problem Detection** — Catch issues before users are affected  
   *(e.g., CPU usage spikes → investigate before outage happens)*

2. **Performance Optimization** — Track bottlenecks and improve speed  
   *(e.g., API response time trending upward → optimize the query)*

3. **SLA Compliance** — Ensure system performance meets agreed uptime/speed  
   *(e.g., 99.9% uptime guarantee)*

4. **Cost Management** — Identify underutilized resources and optimize  
   *(e.g., over-provisioned servers running at 10% CPU)*

### Why Care About Logging?

1. **Debugging & Troubleshooting** — Diagnose problems faster  
   *(e.g., stack trace leads directly to buggy code)*

2. **Auditing & Compliance** — Track user actions for regulatory requirements  
   *(e.g., who deleted this record? logs tell you)*

3. **Usage Analysis** — Understand user behavior to improve product  
   *(e.g., which features are used most?)*

4. **Incident Response** — Determine root cause and fix quickly  
   *(e.g., what happened during the 3am outage?)*

---

## 5. Observability — The Big Picture

> 💡 **Simple Definition:** Observability is like having X-ray vision into your system. Even if something unexpected breaks, you can figure out what's wrong without having to guess.

**Observability** = The ability to understand the internal state of a system based on its external outputs.

```
              OBSERVABILITY
             /      |       \
            ↓       ↓        ↓
         Metrics   Logs    Traces
            |       |        |
            ↓       ↓        ↓
        Monitoring Logging Tracing
            |       |        |
     "What's    "Why is   "How is
     happening?" it broken?" it happening?"
```

### Observability vs Monitoring

| Aspect | Monitoring | Observability |
|--------|-----------|---------------|
| Approach | Watches known metrics | Understands unknown failures |
| Questions | "Is it broken?" | "Why is it broken?" |
| Coverage | Pre-defined checks | Any state of the system |
| Tools | Dashboards, alerts | Metrics + Logs + Traces combined |

---

## 6. The Three Pillars: Metrics, Logs, Traces

### 📊 Pillar 1: Metrics

**Metrics** are numerical measurements of system performance collected over time.

```
Examples:
  - CPU usage: 75%
  - Memory usage: 4.2 GB
  - HTTP request latency: 200ms
  - Error rate: 0.5%
  - Requests per second: 1200 req/s
```

> Think of metrics like your smartwatch data — numbers that change over time.

**Types of Metrics:**
- **Counter** — Only goes up (e.g., total requests)
- **Gauge** — Goes up and down (e.g., CPU %, memory)
- **Histogram** — Distribution of values (e.g., response time buckets)

---

### 📄 Pillar 2: Logs

**Logs** are immutable, timestamped records of discrete events.

```
Example:
  2025-02-16 10:23:45 ERROR Failed to connect to database
  2025-02-16 10:23:46 INFO  Retrying connection... attempt 1/3
  2025-02-16 10:23:47 FATAL Max retries exceeded. Shutting down.
```

> Think of logs like a detailed diary — every event is written down.

**Types of Logs:**
- **Application Logs** — Events from your code
- **System Logs** — OS-level events (`/var/log/syslog`)
- **Access Logs** — HTTP requests (Nginx, Apache)
- **Audit Logs** — Security and user action tracking
- **Error Logs** — Failures and exceptions

---

### 🔍 Pillar 3: Traces

**Traces** represent a single request's journey through multiple services.

```
User clicks "Buy Now"
     │
     ├─► API Gateway (10ms)
     │        │
     ├─► Auth Service (120ms)
     │        │
     ├─► Product Service (45ms)
     │        │
     ├─► Payment Service (300ms)  ← SLOW! bottleneck here
     │        │
     └─► Database (20ms)
     
Total: 495ms — why so slow? Traces show it's Payment Service!
```

> Think of traces like GPS tracking for a request — you can see exactly where it went and where it got stuck.

### Summary Table

| Pillar | Data Type | Purpose | Example |
|--------|-----------|---------|---------|
| **Metrics** | Numbers over time | Health & performance | CPU 75%, latency 200ms |
| **Logs** | Text events | Debugging & forensics | `ERROR: DB connection failed` |
| **Traces** | Request journeys | Finding bottlenecks | 300ms in Payment Service |

---

## 7. Monitoring vs Logging vs Alerting

| Aspect | Monitoring | Logging | Alerting |
|--------|-----------|---------|---------|
| **Purpose** | Track health & performance over time | Record detailed events for debugging | Notify humans when action needed |
| **Data Type** | Metrics (numbers) | Text (structured or unstructured) | Derived from metrics or logs |
| **Typical Use** | Dashboards, graphs, SLOs | Debugging, audits, forensics | PagerDuty, Slack, email |
| **Example** | CPU > 80% for 5 minutes | "User john failed login 3 times" | Alert when error rate > 1% |

### How They Work Together (Real Scenario)

```
STEP 1: Monitoring detects error rate spiked to 5%
          ↓
STEP 2: Alerting pages the on-call engineer via PagerDuty
          ↓
STEP 3: Engineer checks Logs → "database connection refused"
          ↓
STEP 4: Engineer finds root cause → DB ran out of connections
          ↓
STEP 5: Fix applied, error rate drops back to 0%
```

---

## 8. Common Tools Overview

| Category | Open Source / Free | Paid / Enterprise |
|----------|--------------------|-------------------|
| **Metrics** | Prometheus, Graphite, InfluxDB | Datadog, New Relic, AWS CloudWatch |
| **Logging** | ELK Stack, Loki, Graylog | Splunk, Sumo Logic, Datadog Logs |
| **Tracing** | Jaeger, Zipkin | Datadog APM, AWS X-Ray, Dynatrace |
| **Visualization** | Grafana, Kibana, Chronograf | Datadog Dashboards, New Relic |
| **Alerting** | Alertmanager, Grafana Alerts | PagerDuty, Opsgenie, VictorOps |

---

## 9. Production-Level Tools (R&D)

### 🔵 Prometheus (Open Source — Most Popular for Metrics)

**What it does:** Scrapes metrics from your applications at regular intervals and stores them as time-series data.

```
Architecture:
  App (exposes /metrics) → Prometheus scrapes → Stores in TSDB → Grafana visualizes

Key Features:
  ✅ Pull-based scraping model
  ✅ Powerful query language: PromQL
  ✅ Built-in alerting rules
  ✅ Works great with Kubernetes
  
Use Case: Monitoring microservices, Kubernetes clusters
Pricing: FREE (open source)
Who uses it: SoundCloud (created it), Reddit, DigitalOcean
```

**Sample PromQL Query:**
```promql
# HTTP error rate over last 5 minutes
rate(http_requests_total{status="500"}[5m])

# CPU usage percentage
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)
```

---

### 📈 Grafana (Open Source — Visualization King)

**What it does:** Creates beautiful dashboards from any data source (Prometheus, Loki, Elasticsearch, etc.)

```
Key Features:
  ✅ 100+ data source integrations
  ✅ Drag-and-drop dashboard builder
  ✅ Alerting & notifications built-in
  ✅ Grafana Cloud (managed service available)
  
Pricing: Open Source FREE | Grafana Cloud starts at $0 (free tier), ~$8/user/month paid
Who uses it: Twitter, PayPal, eBay
```

---

### 🟠 ELK Stack (Elasticsearch + Logstash + Kibana)

**What it does:** Collect, process, store, and visualize logs at massive scale.

```
Flow:
  App Logs → Logstash (collect & parse) → Elasticsearch (store & index) → Kibana (visualize)

Key Features:
  ✅ Handles petabytes of log data
  ✅ Full-text search on logs
  ✅ Real-time log streaming
  ✅ APM (Application Performance Monitoring) support

Pricing: Open Source FREE | Elastic Cloud starts at ~$16/month
Who uses it: Netflix, LinkedIn, Walmart
```

**Alternative:** **Grafana Loki** — like ELK but lighter, only indexes labels (not full text), much cheaper to run.

---

### 🐶 Datadog (Paid — Enterprise Favorite)

**What it does:** All-in-one observability platform — metrics, logs, traces, APM, security, synthetics.

```
Key Features:
  ✅ 500+ integrations (AWS, GCP, Azure, Kubernetes, etc.)
  ✅ AI-powered anomaly detection
  ✅ End-to-end distributed tracing (APM)
  ✅ Real User Monitoring (RUM)
  ✅ Infrastructure maps
  ✅ Log Management with ML

Pricing: 
  - Infrastructure: ~$15-23/host/month
  - Log Management: ~$0.10/GB ingested
  - APM: ~$31/host/month
  
Who uses it: Samsung, Airbnb, Peloton, 20,000+ companies
Best for: Enterprises wanting ONE tool for everything
```

---

### 🔴 New Relic (Paid — Full-Stack Observability)

**What it does:** APM-first platform with full observability — code-level insights, infrastructure, logs.

```
Key Features:
  ✅ Deep code-level performance tracing
  ✅ Browser & mobile monitoring
  ✅ Synthetic monitoring (test your app 24/7)
  ✅ Vulnerability management
  ✅ AI-powered incident intelligence

Pricing:
  - Free tier: 100 GB/month data ingest
  - Standard: $0.30/GB after free tier
  - Users: $99-349/user/month (full platform)

Who uses it: GitHub, Epic Games, Domino's
Best for: Dev teams wanting deep application insights
```

---

### 🔶 Splunk (Paid — Enterprise Log Management)

**What it does:** Industry leader in log management, SIEM (security), and operational intelligence.

```
Key Features:
  ✅ Handles massive log volumes
  ✅ Powerful SPL (Search Processing Language)
  ✅ Security Information & Event Management (SIEM)
  ✅ IT Service Intelligence (AI-driven)
  ✅ On-premise + Cloud options

Pricing:
  - Enterprise: ~$150/GB/day (very expensive!)
  - Cloud: Starts ~$2000/month
  - Free: 500 MB/day (dev only)

Who uses it: US Government, Banks, Fortune 500
Best for: Large enterprises, security/compliance heavy industries
```

---

### 🟢 AWS CloudWatch (Paid — Cloud Native)

**What it does:** Native monitoring for all AWS services — no agent setup needed for AWS resources.

```
Key Features:
  ✅ Native integration with 70+ AWS services
  ✅ Log Groups & Log Streams
  ✅ CloudWatch Alarms → SNS → Lambda
  ✅ Container Insights for ECS/EKS
  ✅ Application Insights for .NET, Java apps

Pricing:
  - Metrics: First 10 custom metrics free, then $0.30/metric/month
  - Logs: $0.50/GB ingested, $0.03/GB storage
  - Alarms: $0.10/alarm/month

Best for: Teams already on AWS
```

---

### 🔵 Jaeger & Zipkin (Open Source — Distributed Tracing)

**Jaeger** (by Uber) and **Zipkin** (by Twitter) — both are open source distributed tracing systems.

```
Jaeger Features:
  ✅ Visualize end-to-end traces
  ✅ Find performance bottlenecks
  ✅ Supports OpenTelemetry (industry standard)
  ✅ Adaptive sampling

Zipkin Features:
  ✅ Simpler and lighter than Jaeger
  ✅ Good for smaller microservice setups
  ✅ Supports multiple storage backends

Pricing: Both FREE (open source)
```

---

### 🌐 OpenTelemetry (The Future Standard)

> **This is the most important modern concept to understand!**

**What it is:** A vendor-neutral, open standard for collecting metrics, logs, and traces — works with ANY tool.

```
Without OpenTelemetry:
  App → Datadog SDK (locked in to Datadog)

With OpenTelemetry:
  App → OpenTelemetry SDK → OTEL Collector → Any backend
                                               (Jaeger, Prometheus, Datadog, etc.)

Benefits:
  ✅ No vendor lock-in
  ✅ One SDK for all 3 pillars
  ✅ Industry standard (CNCF project)
  ✅ Supported by all major vendors
```

---

## 10. Architecture of Monitoring & Logging Stack

```
┌─────────────────────────────────────────────────────┐
│                   YOUR SYSTEM                       │
│   ┌──────────────┐    ┌──────────────┐             │
│   │ App/Service 1│    │ App/Service 2│             │
│   └──────┬───────┘    └──────┬───────┘             │
│          │                   │                      │
│          └─────────┬─────────┘                      │
│                    ↓                                │
│          ┌─────────────────┐                        │
│          │ Agent/Exporter  │  ← Beats, Fluentd,    │
│          │                 │    Prometheus Agent    │
│          └────────┬────────┘                        │
│                   ↓                                 │
│          ┌─────────────────┐                        │
│          │    Collector    │  ← Logstash, OTEL     │
│          │  (Parse/Filter) │    Collector           │
│          └────────┬────────┘                        │
│                   ↓                                 │
│          ┌─────────────────┐                        │
│          │     Storage     │  ← Elasticsearch,     │
│          │                 │    Prometheus TSDB     │
│          └────────┬────────┘                        │
│                   ↓                                 │
│   ┌───────────────┴──────────────┐                  │
│   ↓                              ↓                  │
│ ┌──────────┐            ┌──────────────┐            │
│ │Dashboard │            │ Alert System │            │
│ │(Grafana) │            │ (PagerDuty)  │            │
│ └──────────┘            └──────────────┘            │
└─────────────────────────────────────────────────────┘
```

**Data Flow Explained:**

1. **App/Services** generate metrics, logs, traces
2. **Agent/Exporter** collects raw data from the source (runs on the same machine)
3. **Collector** parses, filters, enriches, and forwards data
4. **Storage** persists the data for querying
5. **Dashboard** (Grafana, Kibana) visualizes the data
6. **Alert System** sends notifications when thresholds are breached

---

## 11. Linux Commands for Monitoring & Logging

### 🖥️ System Monitoring Commands

#### CPU Monitoring

```bash
# Real-time CPU, memory, process stats
top

# Better version of top (interactive, color)
htop

# CPU info (cores, model)
lscpu

# CPU usage per core (snapshot)
mpstat -P ALL 1

# CPU stats every 2 seconds, 5 times
vmstat 2 5

# Show processes sorted by CPU usage
ps aux --sort=-%cpu | head -20
```

#### Memory Monitoring

```bash
# Show memory usage (human readable)
free -h

# Detailed memory stats
cat /proc/meminfo

# Top memory consumers
ps aux --sort=-%mem | head -20

# Memory usage over time
vmstat -s

# Show memory per process
pmap <PID>
```

#### Disk Monitoring

```bash
# Disk space usage (human readable)
df -h

# Disk usage of a directory
du -sh /var/log/*

# Sort directories by size
du -sh /* 2>/dev/null | sort -rh | head -20

# Real-time disk I/O stats
iostat -xz 1

# Monitor disk I/O per process
iotop

# Check disk health
smartctl -a /dev/sda
```

#### Network Monitoring

```bash
# Active network connections
netstat -tuln

# Better version (same info, faster)
ss -tuln

# Network interface stats
ifconfig
ip addr show

# Real-time network bandwidth per process
nethogs

# Network traffic analysis
iftop

# Check open ports
nmap localhost

# Ping and trace route
ping google.com
traceroute google.com

# DNS lookup
nslookup google.com
dig google.com
```

#### Process Monitoring

```bash
# List all running processes
ps aux

# Find a specific process
ps aux | grep nginx

# Process tree (parent-child relationships)
pstree

# Monitor a specific process in real-time
watch -n 1 "ps aux | grep your_app"

# Kill a process
kill <PID>
kill -9 <PID>   # Force kill

# Find PID by process name
pidof nginx
pgrep nginx
```

---

### 📄 Log Viewing Commands

#### Basic Log Viewing

```bash
# View entire log file
cat /var/log/syslog

# View last 100 lines
tail -100 /var/log/syslog

# Follow log in real-time (live tail)
tail -f /var/log/syslog

# Follow last 50 lines in real-time
tail -n 50 -f /var/log/nginx/error.log

# View first 20 lines
head -20 /var/log/syslog

# View log page by page (press 'q' to quit)
less /var/log/syslog
```

#### Searching Logs

```bash
# Search for a keyword in log file
grep "ERROR" /var/log/app.log

# Case-insensitive search
grep -i "error" /var/log/app.log

# Search with line numbers
grep -n "ERROR" /var/log/app.log

# Show 3 lines before and after match (context)
grep -C 3 "ERROR" /var/log/app.log

# Search in all files in directory
grep -r "failed" /var/log/

# Search and count occurrences
grep -c "ERROR" /var/log/app.log

# Exclude a pattern
grep -v "DEBUG" /var/log/app.log

# Multiple patterns
grep -E "ERROR|WARN|FATAL" /var/log/app.log

# Live tail + filter
tail -f /var/log/app.log | grep "ERROR"
```

#### Systemd Logs (journalctl)

```bash
# View all system logs
journalctl

# View logs for a specific service
journalctl -u nginx
journalctl -u mysql

# Follow logs in real-time
journalctl -f

# Logs from last 1 hour
journalctl --since "1 hour ago"

# Logs between dates
journalctl --since "2025-01-01" --until "2025-01-02"

# Show only errors
journalctl -p err

# Show logs with specific priority levels
# 0=emerg, 1=alert, 2=crit, 3=err, 4=warning, 5=notice, 6=info, 7=debug
journalctl -p 3   # errors and above

# Last 50 lines
journalctl -n 50

# Show kernel logs only
journalctl -k

# Disk usage of logs
journalctl --disk-usage
```

#### Important Log File Locations

```bash
# System logs
/var/log/syslog          # General system messages (Debian/Ubuntu)
/var/log/messages         # General system messages (CentOS/RHEL)
/var/log/kern.log         # Kernel logs
/var/log/dmesg            # Boot/hardware messages

# Authentication logs
/var/log/auth.log         # Login attempts, sudo, SSH (Ubuntu)
/var/log/secure           # Same on CentOS/RHEL

# Application logs
/var/log/nginx/           # Nginx access & error logs
/var/log/apache2/         # Apache logs
/var/log/mysql/           # MySQL logs

# Package manager logs
/var/log/apt/             # apt install/upgrade logs

# View boot messages
dmesg
dmesg | grep -i error
dmesg | grep -i "failed"
```

#### Log Analysis Commands

```bash
# Count errors per hour (useful for trending)
grep "ERROR" /var/log/app.log | awk '{print $1, $2}' | cut -c1-13 | sort | uniq -c

# Top 10 IP addresses hitting your web server
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10

# Most common error messages
grep "ERROR" /var/log/app.log | awk '{$1=$2=$3=""; print $0}' | sort | uniq -c | sort -rn | head -10

# Log file size check
ls -lh /var/log/

# Rotate logs manually
logrotate -f /etc/logrotate.conf

# Monitor multiple log files simultaneously
multitail /var/log/nginx/error.log /var/log/app.log
```

---

### ⚡ Advanced Monitoring Commands

```bash
# System summary (all-in-one)
glances

# Load average (1, 5, 15 minute averages)
uptime
cat /proc/loadavg

# Open file descriptors (useful for debugging "too many open files")
lsof | wc -l
lsof -p <PID>

# System calls made by a process (debugging)
strace -p <PID>

# Performance profiling
perf top

# Check if a port is open
telnet localhost 8080
nc -zv localhost 8080

# Firewall rules
iptables -L -n
ufw status

# Scheduled jobs (cron)
crontab -l
cat /etc/cron.d/*
```

---

## 12. Best Practices

### ✅ DO's

**1. Define Clear Objectives**
- Know what you want to monitor before setting it up
- Examples: response time < 500ms, error rate < 1%, uptime > 99.9%

**2. Use Structured Logging (JSON)**
```json
{
  "timestamp": "2025-02-16T10:23:45Z",
  "level": "error",
  "message": "Failed to connect to database",
  "service": "UserService",
  "userId": 42,
  "traceId": "abc123",
  "hostname": "server-1"
}
```
> Why JSON? It's machine-readable, searchable, and can be parsed by any logging tool.

**3. Add Useful Tags & Metadata**
```
Always include:
  - service name
  - environment (prod/staging/dev)
  - hostname
  - trace/request ID
  - user ID (if applicable)
```

**4. Set Up Meaningful Alerts (not too many!)**
- Alert on **symptoms**, not causes (e.g., alert on "users can't checkout" not "CPU high")
- Avoid alert fatigue — too many false alerts = engineers ignore them
- Use escalation policies (page on-call → team → manager)

**5. Use the USE Method for Infrastructure:**
- **U**tilization — How busy is the resource? (CPU 80%)
- **S**aturation — Is it overloaded? (queue depth growing)
- **E**rrors — Is it failing? (disk errors)

**6. Use the RED Method for Services:**
- **R**ate — Requests per second
- **E**rrors — Error rate
- **D**uration — Response time (latency)

### ❌ DON'Ts

- Don't log sensitive data (passwords, credit cards, PII)
- Don't log everything at DEBUG level in production (too noisy, expensive)
- Don't ignore logs — review them regularly
- Don't create alerts without runbooks (on-call needs to know what to do)
- Don't store logs forever — implement retention policies

---

## 🗺️ Quick Reference: Tool Decision Guide

```
Starting fresh? Small team?
  → Prometheus + Grafana + Loki (open source, free, powerful)

Already on AWS?
  → Start with CloudWatch (native, no setup needed)

Enterprise with budget?
  → Datadog (all-in-one, best UX, expensive)

Security/Compliance heavy?
  → Splunk (industry leader, very expensive)

Large scale logging only?
  → ELK Stack or Sumo Logic

Need distributed tracing?
  → Jaeger (free) or Datadog APM (paid)

Want vendor flexibility?
  → OpenTelemetry SDK → send anywhere
```

---

## 📝 Summary

```
MONITORING  → Numbers over time → Prometheus, Datadog, CloudWatch
LOGGING     → Events & errors  → ELK Stack, Loki, Splunk
TRACING     → Request journeys → Jaeger, Zipkin, Datadog APM
ALERTING    → Notifications    → PagerDuty, Alertmanager, Opsgenie
VISUALIZATION → Dashboards     → Grafana, Kibana, Datadog

The goal: Full Observability
= Know WHAT is happening (Metrics)
+ Know WHY it happened (Logs)  
+ Know HOW it happened (Traces)
```

---

*Notes prepared from Day 1 material — Monitoring & Logging DevOps Course*  
*R&D additions: Production tools research, Linux command reference*
