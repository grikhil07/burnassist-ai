#!/bin/bash

# =================================================================
# AWS EC2 SETUP SCRIPT FOR BURN DETECTION PROJECT (UBUNTU)
# =================================================================

echo "🚀 Starting Ubuntu EC2 Setup..."

# 1. Update system
sudo apt-get update -y
sudo apt-get upgrade -y

# 2. Install Docker
echo "🛠 Installing Docker..."
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 3. Add user to docker group
sudo usermod -aG docker $USER

# 4. Install Docker Compose (as a standalone binary for compatibility with the project command)
echo "🛠 Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 5. Swap file (Skip if already exists)
if [ -f /swapfile ]; then
    echo "✅ Swap file already exists."
else
    echo "🛠 Creating 2GB Swap file for RAM stability..."
    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    echo '/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab
fi

echo "✅ Ubuntu Setup complete! Please log out and log back in (or run 'newgrp docker')."
echo "Then, run: docker-compose up -d --build"
