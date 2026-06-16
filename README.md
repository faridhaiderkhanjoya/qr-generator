# QR Code Generator

A responsive QR Code Generator built with Python and Flask that allows users to generate QR codes from valid website URLs.

## Live Demo

https://qr-generator-wmp1.onrender.com/

## Features

* Generate QR codes from website URLs
* Responsive design (Desktop & Mobile Friendly)
* Download generated QR codes
* URL validation
* Automatic cleanup of old QR images
* Deployed on Render

## Tech Stack

* Python
* Flask
* HTML
* CSS
* Git
* GitHub
* Docker
* Render

## Project Workflow

Local Development → Git → GitHub → Render → Live Deployment

After connecting GitHub with Render, every push to the repository automatically triggers a new deployment, providing a basic CI/CD workflow.

## Docker

### Build Docker Image

```bash
docker build -t qr-generator .
```

### Run Docker Container

```bash
docker run -p 5000:5000 qr-generator
```

### Access Application

```text
http://localhost:5000
```

## Repository

https://github.com/faridhaiderkhanjoya/qr-generator

## Author

Farid Haider
