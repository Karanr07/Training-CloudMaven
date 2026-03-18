# Docker Training: Introduction & Best Practices

## Docker
Docker is a platform that is based on the idea of software containers. The code, libraries, system tools, and configurations required to run an application are all included in these self-contained containers.

---

## Why we use Docker

### Consistency
It means you can run the application on any server and it will run consistently.

Sometimes a developer might spend hours debugging an issue that doesn't exist on their local machine, only to discover that the problem is related to a different library version on the production server.

Docker solves this problem by packaging everything together.

### Faster Deployment
We do not need to install many things manually. Through Docker we can deploy applications faster.

### Efficient Resource Usage
Docker containers are lightweight. We do not need to install a full operating system for every application, so it uses fewer system resources.

### Isolation of Applications
Each application runs in its own container.

If one application crashes, the other applications are not affected.

### Huge Ecosystem & Community
Many developers work with Docker because it is open source.

There are many ready-made images available that we can directly use for our projects.

---

## What is a Container and how it is different from a Virtual Machine

### Container
Containers share the host OS kernel.

This means they only include the required libraries and binaries needed to run the application and Docker engine.

Because they do not run a full operating system, containers are lightweight.

Also, in containers we can run different versions of packages in different containers at the same time.

### Virtual Machine
Virtual Machines require a hypervisor and a full operating system to run.

Because of this, they become heavy and consume more resources.

Also in VMs, running multiple versions of the same package at the same time can be more difficult.

---

## Docker Architecture
Docker architecture includes 4 main components.

### Docker Client (CLI / API)
We use Docker through the client using CLI or API.

Example CLI commands:

```
docker pull
docker ps
docker build
```

### Docker Daemon (Runs Containers)
The Docker daemon is like the brain of Docker.

It is responsible for running and managing containers.

### Docker Images & Containers

**Image**

An image is a blueprint. It includes the software, operating system, and dependencies required to run the application.

**Container**

A container is a running instance of an image.

When we run an image, it creates a container where the application actually runs.

### Docker Hub / Registry
Docker Hub or a registry is used to store Docker images.

We can store our images publicly or privately.

---

## Volumes → Persist Data

If a container is terminated and we have not attached a volume, then the logs and data inside the container are deleted.

To handle this problem, we use Docker volumes so that data can persist.

---

## Networks → Communication Between Containers

To allow Docker containers to communicate with each other, we use Docker networks.

---

## Common Docker Commands

```
docker ps → list running containers
docker images → list images
docker build -t app . → build image
docker run -p 8080:80 app → run container
docker exec -it <id> bash → access container
docker ps -a → see stopped containers
docker logs <container-id> → check logs of a container
```

We mainly use `docker logs` to check why a container is stopping or what is happening inside it.

---

## Dockerfile Example

```
FROM python:3.11-slim
```

In this we specify the base image that we need to run our application.

```
WORKDIR /app
```

When we build an image from a Dockerfile, it creates a working directory where application files will be stored.

```
COPY requirements.txt .
```

Copying the dependency file into the `/app` directory (`.` means current directory).

```
RUN pip install -r requirements.txt
```

Installing the required dependencies.

```
COPY . .
```

Copying the application code into the `/app` folder so the application image can run properly.

```
CMD ["python", "app.py"]
```

This command is used to run the application when the container starts.

The command format may change depending on the programming language used.

---

## RUN vs CMD

### RUN
RUN executes during the image build process.

### CMD
CMD executes when the container starts.

---

## Best Practices

### Use Lightweight Images
Use small images so that containers start faster and use fewer resources.

### Multi-Stage Build
Multi-stage builds help make images smaller.

For example, when we use a large image like `python:3.11` for building the application, we only copy the required dependencies and binaries into a smaller runtime image. This reduces the final image size.

### Do Not Run Containers as Root
For security reasons, we should not run containers as the root user.

If a container runs as root, the application inside the container also runs as root.

If a hacker compromises the application, they may gain root access and modify or delete files.

Therefore running containers as a non-root user is considered a best practice.

### Keep Images Small
Always keep Docker images small by installing only required dependencies and removing unnecessary files.

### .dockerignore
`.dockerignore` works similar to `.gitignore`.

Files or folders like logs, `node_modules`, or other unnecessary dependencies that we do not want inside the image should be listed in `.dockerignore`.
