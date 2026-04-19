# Standard Operating Procedures (SOP): Platform Operations

**Document ID**: OPS-SOP-001  
**Authorized Roles**: DevOps / System Administrators  

## 1. Service Management
Administrative operations are performed via Docker Compose. All commands must be executed from the root project directory (`~/burn_project`).

### 1.1 Service Lifecycle
- **System Start**: `docker-compose up -d --build`
- **Graceful Shutdown**: `docker-compose down`
- **Component Restart**: `docker-compose restart [web|nginx]`

## 2. Monitoring & Troubleshooting
Health checks must be performed weekly to ensure model inference stability.

### 2.1 Health Verification
| Check | Command | Expected State |
| :--- | :--- | :--- |
| **Container Status** | `docker ps` | `Up` (all items) |
| **Log Monitoring** | `docker logs -f burn_app` | Zero `500` Errors |
| **Disk Capacity** | `df -h` | `< 85% Utilized` |

### 2.2 Error Remediation (L1 Support)
1. **Site Unreachable**: Verify Elastic IP association and security group rules. Restart `burn_nginx`.
2. **403 Forbidden**: Ensure `CSRF_TRUSTED_ORIGINS` in `settings.py` matches the accessed URL.
3. **Internal Server Error**: Check `docker logs burn_app`. Common cause is memory pressure; verify Swap file status via `swapon --show`.

## 3. Data Backup Protocol
While the system is currently stateless for core logic, database backups should be performed before major version updates.
- **Command**: `cp db.sqlite3 backups/db_$(date +%F).sqlite3`

## 4. SSL Certificate Maintenance
The system utilizes automated Let's Encrypt certificates.
- **Manual Renewal**: `sudo certbot renew`
- **Re-Generation**: Utilize provided `setup_trusted_ssl.sh` script for fresh domain association.

---
*Confidential - For Internal Use Only*
