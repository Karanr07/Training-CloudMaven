#!/usr/bin/env bash
# =============================================================================
# Traffic Simulation Script
# Generates varied HTTP traffic to the monitored application
# Usage: ./simulate-traffic.sh [duration_seconds] [concurrency]
# =============================================================================

APP_URL="${APP_URL:-http://localhost:3000}"
DURATION="${1:-120}"          # Default: run for 120 seconds
CONCURRENCY="${2:-5}"         # Default: 5 concurrent workers
END_TIME=$((SECONDS + DURATION))

# Color output
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'

log() { echo -e "${CYAN}[$(date '+%H:%M:%S')]${NC} $1"; }
success() { echo -e "${GREEN}[$(date '+%H:%M:%S')] ✓${NC} $1"; }
warn() { echo -e "${YELLOW}[$(date '+%H:%M:%S')] ⚠${NC} $1"; }

# Endpoints with relative weights
ENDPOINTS=(
  "/"           "/" "/"           "/"           # 4x weight — most common
  "/health"     "/health"                        # 2x weight
  "/api/data"   "/api/data"   "/api/data"       # 3x weight
  "/api/slow"                                    # 1x weight — slow endpoint
  "/api/error"                                   # 1x weight — generates 500s
)

send_request() {
  local endpoint="${ENDPOINTS[$RANDOM % ${#ENDPOINTS[@]}]}"
  local http_code
  http_code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "${APP_URL}${endpoint}")
  echo "$endpoint → HTTP $http_code"
}

worker() {
  local worker_id=$1
  log "Worker $worker_id started"
  while [ $SECONDS -lt $END_TIME ]; do
    result=$(send_request)
    # Random sleep between requests: 0.1s to 1.0s
    sleep "0.$(( RANDOM % 9 + 1 ))"
  done
  log "Worker $worker_id finished"
}

# ── Main ──────────────────────────────────────────────────────────────────────
echo ""
echo -e "${CYAN}╔══════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║      Traffic Simulation Starting         ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════╝${NC}"
echo ""
log "Target:      ${APP_URL}"
log "Duration:    ${DURATION} seconds"
log "Concurrency: ${CONCURRENCY} workers"
echo ""

# Verify app is reachable
if ! curl -sf "${APP_URL}/health" > /dev/null; then
  warn "App not reachable at ${APP_URL} — is it running?"
  exit 1
fi
success "App is reachable"
echo ""

# Start workers in background
for i in $(seq 1 "$CONCURRENCY"); do
  worker "$i" &
done

# Progress indicator
while [ $SECONDS -lt $END_TIME ]; do
  remaining=$((END_TIME - SECONDS))
  printf "\r${YELLOW}  ⏱  Running... %3d seconds remaining  ${NC}" "$remaining"
  sleep 2
done

wait   # Wait for all workers to finish
echo ""
echo ""
success "Traffic simulation complete!"
echo ""
log "Check your Grafana dashboards at: http://localhost:3001"
log "  - Dashboard 1: Infrastructure Monitoring"
log "  - Dashboard 2: Application Monitoring"
echo ""
