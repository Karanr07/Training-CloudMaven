# Docker - Day 2

## Running a Website Using Docker and Publishing Image to GitHub Container Registry

## Objective

The objective of this task is to containerize a simple static website using Docker, build a Docker image, run the container locally, and publish the Docker image to the GitHub Container Registry. Finally, a Pull Request is created to submit the changes.

---

## Project Structure

```
Cloud-Maven-Training-Session
│
└── Docker
    └── Day2
        ├── Dockerfile
        ├── index.html
        ├── README.md
        └── screenshots
            ├── docker-build.png
            ├── docker-images.png
            ├── website-running.png
            ├── docker-tag.png
            
```

---

# Step 1: Create a Simple Website

A basic HTML file was created for the website.

### index.html

```html
<!DOCTYPE html>
<html>
<head>
<title>Docker Demo</title>
</head>
<body>
<h1>Hello from Docker Container</h1>
<p>This is a simple website running inside a Docker container.</p>
</body>
</html>
```


---

# Step 2: Create Dockerfile

A Dockerfile was created to package the website inside a container.

### Dockerfile

```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```

### Explanation

* **FROM nginx:latest** → Uses the Nginx base image as the web server
* **COPY** → Copies the HTML file into the Nginx default website directory



---

# Step 3: Build Docker Image

The Docker image was built using the following command:

```
docker build -t website-demo .
```

### Explanation

* **docker build** → Builds the Docker image
* **-t website-demo** → Assigns a name (tag) to the image
* **.** → Uses the current directory as build context

### Screenshot

![Docker Build](screenshots/docker-build.png)

---

# Step 4: Verify Docker Images

To confirm the image was created successfully:

```
docker images
```

This command lists all Docker images available locally.

### Screenshot

![Docker Images](screenshots/docker-image.png)

---

# Step 5: Run Docker Container

Run the container using:

```
docker run -d -p 8080:80 website-demo
```

### Explanation

* **-d** → Runs container in background
* **-p 8080:80** → Maps port 8080 of the host to port 80 inside the container


---

# Step 6: Access the Website

After running the container, the website can be accessed in the browser:

```
http://localhost:8080
```

### Screenshot

![Website Running](screenshots/website-running.png)

---

# Step 7: Tag Image for GitHub Container Registry

The Docker image was tagged before pushing to GitHub Container Registry.

```
docker tag website-demo ghcr.io/YOUR_GITHUB_USERNAME/website-demo:latest
```

### Screenshot

![Docker Tag](screenshots/docker-tag.png)

---

# Step 8: Login to GitHub Container Registry

Login to GitHub Container Registry using a personal access token.

```
echo YOUR_GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
```



---

# Step 9: Push Image to GitHub Container Registry

Push the Docker image to GitHub:

```
docker push ghcr.io/YOUR_GITHUB_USERNAME/website-demo:latest
```

### Screenshot



---

# Step 10: Create Pull Request

Steps followed to create the Pull Request:

```
git checkout -b docker-day2
git add .
git commit -m "Added Docker Day2 website containerization"
git push origin docker-day2
```

Then a Pull Request was created on GitHub to merge the changes.



---

# Conclusion

In this task, a simple static website was successfully containerized using Docker.
A Docker image was created using the Nginx base image, and the website was served through a running Docker container.

The Docker image was then tagged and pushed to the GitHub Container Registry so it can be reused or deployed later. Finally, the implementation was submitted through a Pull Request following collaborative development practices.
