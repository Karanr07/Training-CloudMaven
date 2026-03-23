# CI/CD Fundamentals - Day 1 (GitHub Actions)

## Overview
This document summarizes Day 1 tasks focused on understanding CI/CD fundamentals and GitHub Actions.

## Objectives
- Identify problems in traditional (manual) deployment.
- Understand how GitHub Actions works.
- Learn CI/CD pipeline flow and architecture.

## Task 1: Problems Without CI/CD
### Objective
Analyze the risks and limitations of manual software deployment.

### Identified Problems
- Manual processes increase the chance of human errors.
- No consistent or repeatable deployment process.
- Lack of version tracking and audit trail.
- Difficult to roll back changes.
- Slow and inefficient release cycles.
- High risk of production failures.

### Architecture (Without CI/CD)
`Developer -> Manual Build -> Copy Artifacts -> Server Login -> Manual Deployment -> Fix Issues`

### Explanation
In this approach, every step is performed manually. There is no automation, which leads to inconsistency, delays, and higher risk during deployments.

## Task 2: Exploring GitHub Actions
### Objective
Understand how CI/CD workflows are implemented using GitHub Actions.

### Steps Performed
- Opened a public GitHub repository.
- Navigated to the **Actions** tab.
- Observed workflow execution and configuration.

### Key Observations
#### Triggers
Workflows are triggered by events such as:
- `push`
- `pull_request`
- `schedule`

#### Jobs
Workflows contain one or more jobs such as:
- Build
- Test
- Code quality checks

#### Workflow Purpose
- Automate build and test processes.
- Validate code before merging.
- Ensure code quality and readiness for deployment.

### Architecture (GitHub Actions)
`Code Push -> Trigger -> Workflow -> Job -> Steps -> Execution Result`

### Explanation
- A trigger starts the workflow.
- A workflow defines the pipeline.
- A job runs on a virtual machine (runner).
- Steps execute commands sequentially.

## Task 3: CI/CD Pipeline Flow
### Objective
Identify and arrange the correct stages of a CI/CD pipeline.

### Correct Order
`Write Code -> Build -> Test -> Deploy -> Monitor`

### CI/CD Pipeline Architecture
`Code -> Build -> Test -> Deploy -> Monitor`

### Stage Explanation
- **Code**: Development of application features.
- **Build**: Compile and package the application.
- **Test**: Execute automated tests.
- **Deploy**: Release application to an environment (staging/production).
- **Monitor**: Observe performance and detect issues.

## Key Learnings
- CI/CD eliminates manual deployment challenges.
- Automation improves consistency and reliability.
- Early testing reduces production issues.
- GitHub Actions provides an integrated CI/CD solution.

## Conclusion
CI/CD enables efficient and reliable software delivery by automating build, test, and deployment processes. GitHub Actions simplifies implementing CI/CD pipelines directly within the repository.

