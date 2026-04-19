# Deployment & Operations Cheat Sheet

Use this guide for ongoing maintenance, updates, and troubleshooting of your Burn Detection System on AWS.

## 1. Key Deployment Commands
Run these from inside the `~/burn_project` directory on your EC2 instance:

| Command | Description |
| :--- | :--- |
| `docker-compose up -d --build` | Rebuild and start all containers in background |
| `docker-compose down` | Stop and remove all containers |
| `docker ps` | List all running containers and their status |
| `docker-compose logs -f` | View real-time logs for all services |
| `docker logs -f burn_app` | View specific logs for the Django application |

## 2. File Uploading (From Your Mac)
Run these commands from your local project root. Replace `your-key.pem` with your actual key file.

```bash
# Uploading Settings
scp -i "your-key.pem" burn_project/settings.py ubuntu@52.21.4.126:~/burn_project/burn_project/

# Uploading Nginx Config
scp -i "your-key.pem" nginx.conf ubuntu@52.21.4.126:~/burn_project/

# Uploading Certificates (if regenerated)
scp -i "your-key.pem" certs/* ubuntu@52.21.4.126:~/burn_project/certs/
```

## 3. Storage & Maintenance
Since you are on a restricted Free Tier instance, run these periodically to free up space:

| Command | Description |
| :--- | :--- |
| `docker system prune -a` | **CRITICAL**: Deletes unused images/cache (do this if build fails due to space) |
| `df -h` | Check available disk space on your server |
| `free -m` | Check RAM and Swap usage |

## 4. SSL Maintenance (Self-Signed)
If you ever want to regenerate your certificate for a new IP or name:

```bash
# Generate inside the project folder
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout certs/selfsigned.key -out certs/selfsigned.crt -subj "/CN=your_new_ip"
```

## 5. Troubleshooting Sequence
If the site shows "Bad Gateway" or "Site Can't Be Reached":
1. Check if containers are up: `docker ps`
2. If `burn_app` is "Restarting", check why: `docker logs burn_app`
3. Check AWS Security Group for Port 80 and 443 permissions.
4. Verify the Static IP `52.21.4.126` is correctly set in `settings.py` (CSRF) and `nginx.conf`.
