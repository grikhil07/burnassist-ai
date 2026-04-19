# Infrastructure Security & Compliance Review

**Document Code**: SEC-PROD-001  
**Last Audit**: 2026-04-19  
**Security Level**: High

## 1. Security Philosophy
The Burn Detection System adheres to the principle of **Defense in Depth**. Multi-layered security controls are implemented at the network, host, and application levels to safeguard sensitive biomedical image data.

## 2. Encryption & Data Integrity
### 2.1 Encryption in Transit (TLS)
- **Standard**: TLS 1.2 / 1.3 mandated.
- **Certification**: Let's Encrypt (Automated Authority).
- **Endpoint**: `https://burnassistai.online`
- **Protocol**: 2048-bit RSA encryption for all external-facing endpoints.

### 2.2 CSRF & XSS Protection
- **Cross-Site Request Forgery (CSRF)**: Strict origin validation via `CSRF_TRUSTED_ORIGINS`. Trusted origins are restricted to verified domain names and secure proxy headers.
- **XSS Mitigation**: Automatic context-aware output encoding via Django Template Engine.

## 3. Identity & Access Management (IAM)
- **Host Access**: SSH restricted to RSA Key-Pair authentication. Password authentication is globally disabled.
- **Ingress Control**: AWS Security Group implements a "Default Deny" policy. Only designated ports (22, 80, 443) are provisioned.

## 4. Hardening & Vulnerability Management
### 4.1 Production Configuration
- `DEBUG` Mode: **DISABLED** (prevents information leakage).
- `SECURE_PROXY_SSL_HEADER`: Enabled to enforce secure session cookie handling behind the reverse proxy.
- **Volume Isolation**: Media and database persistence are isolated via Docker volume mounts with restricted host permissions.

### 4.2 Logging & Monitoring
All application logs are captured via Docker standard output and rotated to prevent disk exhaustion. Critical errors trigger immediate traceback capture for rapid auditing.

## 5. Compliance Statement
While this system implements high-tier security standards, it is currently in a **Pilot Phase**. Real-world clinical use requires further integration with HIPAA/GDPR compliant storage solutions and formal medical device certification.
