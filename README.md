# Skin Burn Detection System 🏥

A Deep Learning-based web application for classifying skin burn severity (First, Second, and Third Degree) from images or live camera feeds. Designed for fast inference and deployment on low-resource cloud environments.

## 🚀 Features
- **AI Classification**: Uses a VGG16-based neural network.
- **Dual Mode**: Support for image uploads and live camera capture.
- **Production Ready**: Containerized with Docker and Nginx.
- **Secure**: Pre-configured for HTTPS and CSRF protection.
- **Automated**: CI/CD pipeline included for AWS EC2 deployment.

## 🛠 Tech Stack
-   **Backend**: Django (Python 3.11)
-   **AI Engine**: TensorFlow / Keras (CPU-optimized)
-   **Server**: Gunicorn & Nginx
-   **DevOps**: Docker, Docker Compose, GitHub Actions
-   **Hosting**: AWS EC2 (Free Tier compatible)

## 📦 Local Setup
1. Clone the repo:
   ```bash
   git clone <your-repo-url>
   cd burn_project
   ```
2. Run with Docker:
   ```bash
   docker-compose up --build
   ```
3. Access at `http://localhost`.

## ☁️ AWS Deployment
Follow the [Walkthrough Guide](file:///Users/grikhiltt/.gemini/antigravity/brain/9f85dca3-4e8e-4d85-a7e1-ca5d1c40da28/walkthrough.md) for full instructions on setting up the EC2 instance, Elastic IP, and HTTPS.

## 📝 License
This project is for educational/medical research purposes only.
