"""
log_generator.py
Continuously emits structured JSON log lines to /var/log/app/app.log
covering DEBUG, INFO, WARNING, ERROR and CRITICAL levels.
"""

import json
import logging
import os
import random
import time
from datetime import datetime, timezone

LOG_PATH = "/var/log/app/app.log"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# ── Services / endpoints simulated ───────────────────────────────────────────
SERVICES   = ["auth-service", "payment-service", "api-gateway",
               "user-service", "inventory-service", "notification-service"]
ENDPOINTS  = ["/api/login", "/api/checkout", "/api/products",
              "/api/users", "/api/orders", "/api/health"]
HTTP_CODES = [200, 200, 200, 201, 204, 400, 401, 403, 404, 422, 500, 503]
LEVELS     = ["DEBUG", "INFO", "INFO", "INFO", "WARNING", "ERROR", "CRITICAL"]

MESSAGES = {
    "DEBUG":    ["Cache miss for key {key}",
                 "DB query took {ms}ms",
                 "Retrying connection attempt {n}"],
    "INFO":     ["{method} {endpoint} → {code} ({ms}ms)",
                 "User {user_id} authenticated successfully",
                 "Processed {n} records in batch",
                 "Health check passed"],
    "WARNING":  ["Response time {ms}ms exceeds threshold",
                 "Deprecated endpoint called: {endpoint}",
                 "Memory usage at {pct}%"],
    "ERROR":    ["Unhandled exception on {endpoint}: {err}",
                 "Database connection timeout after {ms}ms",
                 "Payment gateway rejected transaction {tx_id}"],
    "CRITICAL": ["Service {service} unreachable – circuit breaker open",
                 "Disk usage at {pct}% – write failures imminent",
                 "OOM kill detected in container {container}"],
}

ERRORS = ["NullPointerException", "TimeoutError", "ConnectionRefusedError",
          "ValueError: invalid literal", "KeyError: 'user_id'"]


def rand_payload(level: str, service: str) -> dict:
    tpl = random.choice(MESSAGES[level])
    msg = tpl.format(
        key=f"user:{random.randint(1000, 9999)}",
        ms=random.randint(5, 3000),
        n=random.randint(1, 500),
        method=random.choice(["GET", "POST", "PUT", "DELETE"]),
        endpoint=random.choice(ENDPOINTS),
        code=random.choice(HTTP_CODES),
        user_id=f"usr_{random.randint(10000, 99999)}",
        pct=random.randint(70, 99),
        err=random.choice(ERRORS),
        tx_id=f"TXN-{random.randint(100000, 999999)}",
        service=random.choice(SERVICES),
        container=f"container_{random.randint(1, 8)}",
    )
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level":     level,
        "service":   service,
        "message":   msg,
        "host":      os.uname().nodename,
        "pid":       os.getpid(),
    }
    # attach request context for non-debug entries
    if level != "DEBUG":
        payload["request_id"] = f"req-{random.randint(1_000_000, 9_999_999)}"
    if level in ("ERROR", "CRITICAL"):
        payload["error_type"] = random.choice(ERRORS).split(":")[0]
        payload["stack_trace"] = f"Traceback (most recent call last):\n  ...\n{payload['error_type']}"
    return payload


def main():
    print(f"[log-generator] Writing logs to {LOG_PATH}", flush=True)
    with open(LOG_PATH, "a", buffering=1) as fh:
        while True:
            level   = random.choice(LEVELS)
            service = random.choice(SERVICES)
            record  = rand_payload(level, service)
            fh.write(json.dumps(record) + "\n")
            print(json.dumps(record), flush=True)

            # Burst errors occasionally to make dashboards interesting
            if random.random() < 0.05:
                for _ in range(random.randint(3, 8)):
                    err_record = rand_payload("ERROR", service)
                    fh.write(json.dumps(err_record) + "\n")

            time.sleep(random.uniform(0.3, 1.5))


if __name__ == "__main__":
    main()
