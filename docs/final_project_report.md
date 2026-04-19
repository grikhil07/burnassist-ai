# Project Report: Skin Burn Detection System Deployment

## 1. Executive Summary
The Skin Burn Detection System has been successfully transitioned from a local development environment to a production-ready, cloud-hosted platform on AWS. The application is now fully accessible via a secure, permanent Static IP address, utilizing containerization for reliability and resource optimization for cost-efficiency.

## 2. Technical Architecture
The system follows a modern, scalable architecture:
- **Frontend/Backend**: Django Web Framework.
- **Deep Learning Inference**: Keras/TensorFlow-CPU (Optimized for low-memory environments).
- **WSGI Server**: Gunicorn (configured with 2 workers and 120s timeout for model loading).
- **Reverse Proxy**: Nginx (serving static files and handling SSL termination).
- **Containerization**: Docker & Docker Compose.

## 3. Key Achievements & Implementations

### A. AWS Free Tier Optimization
- **Memory Management**: Configured a **2GB Linux Swap file** on the EC2 instance to ensure stable loading of the AI model on limited hardware (`t2.micro/t3.small`).
- **Disk Optimization**: Utilized the **30GB AWS Free Tier storage limit** and resized the filesystem to accommodate Docker images and system overhead.
- **Dependency Tuning**: Switched to `tensorflow-cpu` and minimized the Docker image size to prevent "no space left" errors.

### B. Networking & Persistence
- **Elastic IP (Static IP)**: Associated a permanent Static IP (`52.21.4.126`) to the instance, ensuring the application remains reachable even after server restarts.
- **Nginx Serving Layer**: Configured Nginx to serve `static` and `media` files directly from volumes, significantly improving performance and reducing Django's load.

### C. Security Suite
- **Trusted SSL (HTTPS)**: Successfully implemented a verified Let's Encrypt certificate for the custom domain, replacing the self-signed version and enabling the "Green Padlock" in all browsers.
- **Django Security & UI**: 
    - Disabled `DEBUG` mode for production.
    - Configured `CSRF_TRUSTED_ORIGINS` and `SECURE_PROXY_SSL_HEADER` for seamless form submissions.
    - Implemented **Persistent Dark Theme** logic using browser `localStorage`.
- **AWS Security Group**: Configured inbound firewall rules to selectively allow HTTP (80), HTTPS (443), and SSH (22) traffic.

## 4. Current Status
- **Official URL**: [https://burnassistai.online/](https://burnassistai.online/)
- **Fallback URL**: [https://52.21.4.126/](https://52.21.4.126/)
- **Health**: All services (Web and Nginx) are currently `Healthy` and `Running`.
- **Functionality**: Image analysis and real-time prediction are fully operational.

## 5. Future Scalability (Roadmap)
- **CI/CD Integration**: The system is ready for automated GitHub Actions deployment.
- **External Storage**: Potential transition of media files to Amazon S3 for unlimited image storage capacity.
- **Load Balancing**: Ready for Application Load Balancer (ALB) integration if traffic increases.
