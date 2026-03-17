# 🚀 Docker Networking Practical (Day 3)

## 📌 Objective

The objective of this task is to understand and implement Docker networking concepts by deploying a three-tier application and demonstrating different network modes:

* Bridge Network
* Host Network
* None Network

---

## 📂 Project Structure

The project is organized in a structured way:

```
Training-CloudMaven/
│
├── Docker/
│   ├── Day3/
│   │   ├── Three-Tier-Applications/
│   │   ├── screenshots/
```

---

## 🧱 Project Overview

This is a **Three-Tier Application** consisting of:

* **Frontend** → React
* **Backend** → Node.js
* **Database** → MySQL

All services are containerized using Docker and managed via Docker Compose.

---

## ⚙️ Setup Steps

### 1️⃣ Clone Repository

```bash
git clone https://github.com/nahidkishore/Three-Tier-Applications.git
cd Three-Tier-Applications
```

---

### 2️⃣ Build and Run Containers

```bash
docker compose up -d --build
```

---

### 3️⃣ Verify Running Containers

```bash
docker ps
```

---

## 🌐 Docker Networking Implementation

---

## 🔵 1. Bridge Network (Default)

Docker Compose automatically creates a **custom bridge network**.

### Commands:

```bash
docker network ls
docker network inspect three-tier-net
```

### 📸 Screenshots:

* docker-compose → `screenshots/docker-compose.png`
* docker-compose1 → `screenshots/docker-compose1.png`
* docker-inspect → `screenshots/docker-inspect.png`
* docker-inspect1 → `screenshots/docker-inspect1.png`
* docker-inspect1.2 → `screenshots/docker-inspect1.2.png`

### ✅ Observation:

* Containers communicate using service names
* Isolated network created automatically

---

## 🟢 2. Host Network (Windows Workaround)

⚠️ Host networking is not fully supported on Windows Docker Desktop.

### Command Used:

```bash
docker run -d -p 8080:80 --name test-host nginx
```

### Access:

```
http://localhost:8080
```

### 📸 Screenshot:

* host-output → `screenshots/host-output.png`

### ✅ Observation:

* Container accessible via localhost
* Port mapping used instead of true host networking

---

## ⚫ 3. None Network (Isolation)

### Command:

```bash
docker run -it --network none busybox sh
```

### Test:

```bash
ping google.com
```

### 📸 Screenshot:

* none-output → `screenshots/none-output.png`

### ✅ Observation:

* No internet connectivity
* Fully isolated container

---

## 🐳 Docker Build Process

### 📸 Screenshots:

* docker-build → `screenshots/docker-build.png`
* docker-image → `screenshots/docker-image.png`
* docker-tag → `screenshots/docker-tag.png`

---

## ⚠️ Challenges Faced

1. **Docker Compose Image Pull Error**

   * Issue: Docker tried to pull non-existing images
   * Solution: Replaced `image` with `build`

2. **npm ECONNRESET Error**

   * Issue: Network failure during `npm install`
   * Solution: Installed dependencies locally and optimized Dockerfile

3. **Container Naming Conflict**

   * Issue: Duplicate container name
   * Solution: Removed existing container or used new name

---

## 🧠 Key Learnings

* Difference between **image vs build**
* Docker networking types:

  * Bridge → default communication
  * Host → direct access (limited on Windows)
  * None → complete isolation
* Debugging Docker build and network issues
* Container communication using service names

---

## 🎯 Conclusion

Successfully implemented a three-tier application using Docker and demonstrated all major networking modes. This task improved understanding of container networking, troubleshooting, and real-world Docker usage.

---

## 👨‍💻 Author

Karan Rajesh Dwivedi
