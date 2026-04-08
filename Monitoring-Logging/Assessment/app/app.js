const express = require('express');
const client = require('prom-client');

const app = express();
const PORT = 3000;

// ─── Prometheus Registry ───────────────────────────────────────────────────
const register = new client.Registry();

// Collect default Node.js metrics (CPU, memory, event loop, etc.)
client.collectDefaultMetrics({ register });

// ─── Custom Metrics ────────────────────────────────────────────────────────

// Counter: total HTTP requests
const httpRequestsTotal = new client.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code'],
  registers: [register],
});

// Histogram: request duration in seconds
const httpRequestDurationSeconds = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration in seconds',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
  registers: [register],
});

// Counter: application errors
const appErrorsTotal = new client.Counter({
  name: 'app_errors_total',
  help: 'Total number of application errors',
  labelNames: ['type'],
  registers: [register],
});

// Gauge: active connections
const activeConnections = new client.Gauge({
  name: 'app_active_connections',
  help: 'Number of currently active connections',
  registers: [register],
});

// Gauge: simulated active users
const activeUsers = new client.Gauge({
  name: 'app_active_users',
  help: 'Simulated number of active users',
  registers: [register],
});

// ─── Middleware: Track metrics per request ─────────────────────────────────
app.use((req, res, next) => {
  if (req.path === '/metrics') return next();

  const end = httpRequestDurationSeconds.startTimer();
  activeConnections.inc();

  res.on('finish', () => {
    httpRequestsTotal.inc({
      method: req.method,
      route: req.path,
      status_code: res.statusCode,
    });
    end({ method: req.method, route: req.path, status_code: res.statusCode });
    activeConnections.dec();
  });

  next();
});

// ─── Routes ────────────────────────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({
    service: 'monitored-app',
    status: 'running',
    timestamp: new Date().toISOString(),
    endpoints: ['/', '/health', '/api/data', '/api/slow', '/api/error', '/metrics'],
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', uptime: process.uptime() });
});

app.get('/api/data', (req, res) => {
  res.json({
    message: 'Data fetched successfully',
    items: Array.from({ length: 10 }, (_, i) => ({ id: i + 1, value: Math.random() })),
  });
});

app.get('/api/slow', async (req, res) => {
  const delay = Math.floor(Math.random() * 800) + 200; // 200–1000ms
  await new Promise((r) => setTimeout(r, delay));
  res.json({ message: 'Slow response', delay_ms: delay });
});

app.get('/api/error', (req, res) => {
  appErrorsTotal.inc({ type: 'simulated_error' });
  res.status(500).json({ error: 'Simulated server error', code: 'ERR_SIMULATED' });
});

// Prometheus scrape endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

// ─── Simulate Active Users (background task) ──────────────────────────────
setInterval(() => {
  const users = Math.floor(Math.random() * 50) + 10;
  activeUsers.set(users);
}, 5000);

// ─── Start Server ─────────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`✅  App listening on http://localhost:${PORT}`);
  console.log(`📊  Metrics available at http://localhost:${PORT}/metrics`);
});
