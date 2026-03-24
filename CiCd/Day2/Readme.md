# 🚀 GitHub Actions Tasks

---

## ✅ Task 1: Trigger Configuration

### 📌 Scenario

A team wants:

✔ Workflow to run on Pull Requests
✔ Manual execution option

### 🛠️ Solution

```yaml
name: PR Workflow

on:
  pull_request:
    branches:
      - main
  workflow_dispatch:
```

---

## ✅ Task 2: Job Dependency Design

### 📌 Scenario

Build application
Run tests only after build completes

### 🛠️ Solution

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build step
        run: echo "Building application..."

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Test step
        run: echo "Running tests..."
```

---

## ✅ Task 3: Using GitHub Context Variables

### 📌 Task

Print:

✔ Branch name
✔ Commit ID

### 🛠️ Solution

```yaml
- name: Print Branch and Commit
  run: |
    echo "Branch Name: ${{ github.ref }}"
    echo "Commit ID: ${{ github.sha }}"
```

---

## ✅ Task 4: Pull Request Workflow

### 📌 Scenario

Trigger: Pull Request
Job: Build
Job: Test (after build)

### 🛠️ Solution

```yaml
name: PR Workflow

on:
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build
        run: echo "Building project..."

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Test
        run: echo "Testing project..."
```
![PullRequest](screenshots/pulltriger.png)
---

## ✅ Task 5: Docker Build & Push

### 📌 Scenario

Build Docker image
Push to registry using environment variables

### 🛠️ Solution

```yaml
- name: Build, Tag and Push Docker Image
  env:
    REGISTRY: docker.io
    REPOSITORY: my-username/my-app
    IMAGE_TAG: latest

  run: |
    echo "Building Docker image..."
    docker build --build-arg ENV=dev -t $REGISTRY/$REPOSITORY:$IMAGE_TAG .

    echo "Pushing Docker image..."
    docker push $REGISTRY/$REPOSITORY:$IMAGE_TAG

    echo "Removing local image..."
    docker rmi $REGISTRY/$REPOSITORY:$IMAGE_TAG
```
![DockerBuild](screenshots/dockerbuild.png)
---

## 🔥 Final Notes

✔ `pull_request` → triggers workflow on PR
✔ `workflow_dispatch` → manual run
✔ `needs` → job dependency (build → test)
✔ `${{ github.ref }}` → branch name
✔ `${{ github.sha }}` → commit ID

---

## 👨‍💻 Author

Karan Rajesh Dwivedi
