# feat: add ELK-based centralized logging setup

## What was implemented

End-to-end centralized logging pipeline using the ELK stack, deployable with a
single `docker compose up -d --build`.

### Components
| Component | Version | Notes |
|-----------|---------|-------|
| Elasticsearch | 8.12.0 | Single-node, security disabled for dev |
| Kibana | 8.12.0 | Auto-provisioned data view + dashboard |
| Logstash | 8.12.0 | Enrichment pipeline (severity, HTTP tags) |
| Filebeat | 8.12.0 | JSON log shipper |
| log-generator | – | Python app – realistic multi-service logs |

### Log enrichment (Logstash pipeline)
- ISO-8601 timestamp → `@timestamp`
- Normalised log `level` (uppercase)
- Integer `severity` field (1=DEBUG … 5=CRITICAL)
- `alert` tag on ERROR / CRITICAL events
- `http_4xx` / `http_5xx` tags from message patterns
- Filebeat meta-fields cleaned up

## How to test

```bash
git clone <repo-url>
cd elk-logging
docker compose up -d --build

# Wait ~2 minutes for all services to initialise
docker compose ps          # all should show "running" or "exited 0"

# Verify logs are indexed
curl http://localhost:9200/app-logs-*/_count

# Open Kibana
open http://localhost:5601
```

### Verification checklist
- [ ] `docker compose ps` shows all 5 services healthy / running
- [ ] `curl localhost:9200/_cat/indices?v` shows `app-logs-<today>` with docs > 0
- [ ] Kibana Discover → data view **App Logs** shows live log stream
- [ ] KQL filter `level:"ERROR"` returns only error-level documents
- [ ] Dashboard **Application Logs Overview** loads without errors

## Screenshots

> _Attach screenshots of:_
> 1. **Kibana Discover** – showing the log stream with JSON fields expanded
> 2. **Kibana Dashboard** – error count metric + logs over time bar chart + level distribution pie

## Notes
- xpack.security is disabled for local dev convenience. See README for production hardening steps.
- The `kibana-setup` service exits with code 0 after provisioning – this is expected.
