# AWS Production Deployment Walkthrough

Comprehensive guide to the live Skin Burn Detection System.

## 1. Infrastructure (AWS)
- **OS**: Ubuntu 22.04 LTS (Optimized for Docker compatibility).
- **Instance**: `t2.micro` / `t3.small` (Free Tier).
- **Storage**: 30GB EBS (Optimized via `growpart` and `resize2fs`).
- **Persistence**: **Elastic IP** (`52.21.4.126`) attached for permanent access.

## 2. Server Preparation
We ran the following during initialization:
1.  **Swap Space**: Created a 2GB `/swapfile` to provide extra RAM for the AI model.
2.  **Docker Suite**: Installed Docker Engine and Docker Compose.
3.  **Permissions**: Configured the `ubuntu` user for non-sudo Docker access.

## 3. Deployment Flow (Docker)
The app is orchestrated via `docker-compose`:
- **Web Service**: Django + Gunicorn (Python 3.11).
- **Proxy Service**: Nginx (handling Static/Media files and SSL).

```bash
cd ~/burn_project
docker-compose up -d --build
```

## 4. HTTPS & Security
- **Protocol**: HTTPS (Port 443).
- **Encryption**: Self-signed SSL Certificate (Stored in `~/burn_project/certs/`).
- **Django Security**: `DEBUG=False` with `CSRF_TRUSTED_ORIGINS` locked to the Static IP.

## 5. Automation (CI/CD)
The project is set up with **GitHub Actions**:
- **Workflow**: `.github/workflows/deploy.yml`
- **Trigger**: Every push to the `main` branch.
- **Action**: Automate `git pull` and `docker-compose` restart on the EC2 instance.

---

### Key Resources
- [Final Project Report](file:///Users/grikhiltt/.gemini/antigravity/brain/9f85dca3-4e8e-4d85-a7e1-ca5d1c40da28/final_project_report.md)
- [Operations Cheat Sheet](file:///Users/grikhiltt/.gemini/antigravity/brain/9f85dca3-4e8e-4d85-a7e1-ca5d1c40da28/deployment_cheat_sheet.md)
- [CI/CD Implementation Plan](file:///Users/grikhiltt/.gemini/antigravity/brain/9f85dca3-4e8e-4d85-a7e1-ca5d1c40da28/cicd_implementation_plan.md)
