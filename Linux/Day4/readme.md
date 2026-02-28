# Linux Monitoring & Networking Labs

## 📌 Overview

This repository contains hands-on Linux administration and networking labs focused on system monitoring, process analysis, automation, and network traffic inspection.

The tasks demonstrate practical DevOps and system administration skills using Bash scripting and Linux utilities.

---

## 🧪 Lab 1 — Disk Monitoring Script

### Objective

Monitor disk usage and generate alerts when usage exceeds a defined threshold.

### Script: `disk_check.sh`

```bash
#!/bin/bash
set -eu

threshold=80

usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$usage" -gt "$threshold" ]; then
    echo "$(date): Disk usage high - $usage%" >> /tmp/disk_alert.log
fi
```

### Make Executable

```bash
chmod +x disk_check.sh
```

### Run Script

```bash
./disk_check.sh
```

---

## 🌐 Lab 2 — Capture HTTP Traffic

### Objective

Capture TCP handshake and HTTP packets using tcpdump.

### Terminal 1 (Packet Capture)

```bash
sudo tcpdump -i eth0 port 80
```

### Terminal 2 (Generate HTTP Traffic)

```bash
curl http://example.com
```

### Observation

* TCP 3-way handshake (SYN → SYN-ACK → ACK)
* HTTP GET request packets

---

## 🏠 Homework Deliverables

---

### 1️⃣ countargs.sh

Prints all command-line arguments and total count.

```bash
#!/bin/bash

for arg in "$@"
do
    echo "$arg"
done

echo "Total arguments: $#"
```

Run:

```bash
chmod +x countargs.sh
./countargs.sh one two three
```

---

### 2️⃣ Process Using Maximum Memory

Identify the process consuming the most memory.

```bash
ps aux --sort=-%mem | head -1
```

Explanation:

* `ps aux` → Lists running processes
* `--sort=-%mem` → Sorts by memory usage (descending)
* `head -1` → Displays top memory-consuming process

---

### 3️⃣ Largest Directory in `/var/log`

```bash
du -sh /var/log/* | sort -hr | head
```

Displays directories consuming the highest disk space.

---

### 4️⃣ Last 20 SSH Logs

```bash
journalctl -u ssh -n 20
```

Shows recent SSH login activity including successful and failed attempts.

---

### 5️⃣ Schedule Script Using Cron

Open cron editor:

```bash
crontab -e
```

Add:

```bash
*/5 * * * * /home/user/disk_check.sh
```

Runs disk monitoring script every 5 minutes.

---

### 6️⃣ Automation Using systemd Timer

#### Create Service File

`/etc/systemd/system/disk_check.service`

```ini
[Unit]
Description=Disk Monitoring Script

[Service]
ExecStart=/home/user/disk_check.sh
```

#### Create Timer File

`/etc/systemd/system/disk_check.timer`

```ini
[Unit]
Description=Run Disk Check Every 5 Minutes

[Timer]
OnBootSec=1min
OnUnitActiveSec=5min
Unit=disk_check.service

[Install]
WantedBy=timers.target
```

Enable Timer:

```bash
sudo systemctl daemon-reload
sudo systemctl enable disk_check.timer
sudo systemctl start disk_check.timer
```

Verify:

```bash
systemctl list-timers
```

---

## 📂 Repository Structure

```
Linux/
├── disk_check.sh
├── countargs.sh
├── disk_check.service
├── disk_check.timer
└── screenshots/
```

---

## ✅ Skills Demonstrated

* Bash Scripting
* Disk Monitoring
* Process Management
* Log Analysis
* Network Packet Capture
* Task Automation
* Cron Jobs
* systemd Timers

---

## 🚀 Author

**Karan Rajesh Dwivedi**

Aspiring Cloud & DevOps Engineer
