# Complete Linux Mastery Guide
## From Beginner to DevOps Expert

---

## Table of Contents
1. [Linux Filesystem Hierarchy](#1-linux-filesystem-hierarchy)
2. [Users & Groups Management](#2-users--groups-management)
3. [File Permissions & Ownership](#3-file-permissions--ownership)
4. [Process Management](#4-process-management)
5. [SystemD & Services](#5-systemd--services)
6. [Networking Fundamentals](#6-networking-fundamentals)
7. [Docker & Containers](#7-docker--containers)
8. [Namespaces & Isolation](#8-namespaces--isolation)
9. [Package Management](#9-package-management)
10. [System Monitoring & Logs](#10-system-monitoring--logs)
11. [Shell Scripting Essentials](#11-shell-scripting-essentials)
12. [Security Best Practices](#12-security-best-practices)

---

## 1. Linux Filesystem Hierarchy

### Theory
```
/               Root - everything starts here
├── bin         Essential user binaries (ls, cat, cp)
├── boot        Boot loader files (kernel, grub)
├── dev         Device files (hard drives, USB, terminals)
├── etc         Configuration files (system-wide)
├── home        User home directories
├── lib         Shared libraries
├── media       Mount points for removable media
├── mnt         Temporary mount points
├── opt         Optional/Add-on applications ⭐
├── proc        Virtual filesystem (process info)
├── root        Root user's home directory
├── run         Runtime data (PID files)
├── srv         Service data (web servers)
├── sys         Virtual filesystem (kernel/devices)
├── tmp         Temporary files (cleared on reboot)
├── usr         User programs & data
└── var         Variable data (logs, databases)
```

### Why /opt Matters
- **Purpose**: Manual installations, custom apps, Docker deployments
- **Benefits**: 
  - Isolated from system packages
  - Safe during OS upgrades
  - Root-owned by default (secure)
  - Industry standard for production apps

### Hands-On Exercise 1: Explore Filesystem
```bash
# View filesystem hierarchy
tree -L 1 / 2>/dev/null || ls -la /

# Check disk usage
df -h

# See what's in important directories
ls -lh /opt
ls -lh /etc
ls -lh /var/log

# Find large files
sudo find / -type f -size +100M 2>/dev/null | head -10

# Check your current location
pwd

# Navigate and explore
cd /opt
cd /etc
cd ~  # Go to home directory
```

### Hands-On Exercise 2: Create Production Directory Structure
```bash
# Create a professional app structure
sudo mkdir -p /opt/myapp/{backend,frontend,logs,backups,scripts}

# Verify structure
tree /opt/myapp || ls -R /opt/myapp

# Create deployment directories
sudo mkdir -p /opt/{staging,production,dev}

# List with details
ls -lah /opt
```

---

## 2. Users & Groups Management

### Theory

**User**: Individual account on the system
- Has UID (User ID)
- Has home directory
- Has login shell
- Belongs to groups

**Group**: Collection of users with shared permissions
- Has GID (Group ID)
- Used for access control
- Similar to Windows AD groups

**Primary Group**: Default group for user (usually same name)
**Secondary Groups**: Additional groups user belongs to

### Important System Users
```
root        - Superuser (UID 0)
nobody      - Unprivileged user
www-data    - Web server
mysql       - Database
docker      - Docker daemon
```

### Important System Groups
```
sudo        - Can run sudo commands (admin)
docker      - Can use Docker without sudo
adm         - Can read system logs
wheel       - Admin group (RHEL/CentOS)
```

### Hands-On Exercise 3: Complete User & Group Lab

```bash
# ==========================================
# PART 1: Create Groups
# ==========================================

# Create business units
sudo groupadd developers
sudo groupadd operations
sudo groupadd qa
sudo groupadd managers

# Verify groups created
cat /etc/group | grep -E "developers|operations|qa|managers"

# Check GID
getent group developers

# ==========================================
# PART 2: Create Users
# ==========================================

# Create developers
sudo useradd -m -s /bin/bash -c "Alice Developer" alice
sudo useradd -m -s /bin/bash -c "Bob Developer" bob

# Create ops team
sudo useradd -m -s /bin/bash -c "Charlie Ops" charlie
sudo useradd -m -s /bin/bash -c "Diana Ops" diana

# Create QA
sudo useradd -m -s /bin/bash -c "Eve QA" eve

# Create manager
sudo useradd -m -s /bin/bash -c "Frank Manager" frank

# Set passwords
echo "alice:DevPass123" | sudo chpasswd
echo "bob:DevPass123" | sudo chpasswd
echo "charlie:OpsPass123" | sudo chpasswd
echo "diana:OpsPass123" | sudo chpasswd
echo "eve:QAPass123" | sudo chpasswd
echo "frank:MgrPass123" | sudo chpasswd

# Verify users
cat /etc/passwd | grep -E "alice|bob|charlie|diana|eve|frank"

# Check home directories
ls -la /home/

# ==========================================
# PART 3: Assign Users to Groups
# ==========================================

# Add developers to developers group
sudo usermod -aG developers alice
sudo usermod -aG developers bob

# Add ops to operations group
sudo usermod -aG operations charlie
sudo usermod -aG operations diana

# Add QA to qa group
sudo usermod -aG qa eve

# Manager gets access to all groups
sudo usermod -aG developers,operations,qa,managers frank

# Give some users sudo access
sudo usermod -aG sudo alice
sudo usermod -aG sudo charlie
sudo usermod -aG sudo frank

# Verify group membership
groups alice
groups bob
groups charlie
groups frank

# ==========================================
# PART 4: Create Team Workspaces
# ==========================================

# Create team directories
sudo mkdir -p /teams/{dev,ops,qa,management}

# Set group ownership
sudo chown root:developers /teams/dev
sudo chown root:operations /teams/ops
sudo chown root:qa /teams/qa
sudo chown root:managers /teams/management

# Set permissions (group can read/write)
sudo chmod 770 /teams/dev
sudo chmod 770 /teams/ops
sudo chmod 770 /teams/qa
sudo chmod 770 /teams/management

# Create shared documents folder (read-only for all)
sudo mkdir -p /teams/shared
sudo chmod 755 /teams/shared

# Verify permissions
ls -la /teams/

# ==========================================
# PART 5: Test Access Control
# ==========================================

# Switch to alice (developer)
sudo -u alice bash -c '
echo "Alice was here" > /teams/dev/alice.txt
cat /teams/dev/alice.txt
echo "Trying ops folder..."
echo "test" > /teams/ops/alice.txt 2>&1 || echo "ACCESS DENIED (Expected)"
'

# Switch to charlie (ops)
sudo -u charlie bash -c '
echo "Charlie ops log" > /teams/ops/charlie.txt
cat /teams/ops/charlie.txt
echo "Trying dev folder..."
echo "test" > /teams/dev/charlie.txt 2>&1 || echo "ACCESS DENIED (Expected)"
'

# Test manager access (should access all)
sudo -u frank bash -c '
echo "Manager review - Dev" > /teams/dev/frank.txt
echo "Manager review - Ops" > /teams/ops/frank.txt
echo "Manager review - QA" > /teams/qa/frank.txt
ls -lh /teams/*/frank.txt
'

# ==========================================
# PART 6: Docker Access
# ==========================================

# Give developers Docker access
sudo usermod -aG docker alice
sudo usermod -aG docker bob

# Verify
groups alice
groups bob

# Test (requires Docker installed)
sudo -u alice docker ps 2>/dev/null && echo "Alice can use Docker!" || echo "Docker not installed or access denied"

# ==========================================
# PART 7: User Information Commands
# ==========================================

# Who am I?
whoami

# User details
id alice
id

# All logged in users
who

# Last logins
last | head -10

# User info
finger alice 2>/dev/null || getent passwd alice

# All groups
cat /etc/group

# All users
cat /etc/passwd

# ==========================================
# PART 8: Modify Users
# ==========================================

# Change user's shell
sudo usermod -s /bin/zsh alice 2>/dev/null || echo "zsh not installed"

# Change user's home directory
# sudo usermod -d /home/newhome -m alice

# Lock a user account
sudo usermod -L bob
sudo usermod -U bob  # Unlock

# Set account expiration
sudo chage -E 2025-12-31 eve
sudo chage -l eve  # List

# Change user's comment
sudo usermod -c "Alice - Senior Developer" alice

# ==========================================
# PART 9: Delete Users (Cleanup)
# ==========================================

# Remove user but keep home directory
# sudo userdel alice

# Remove user and home directory
# sudo userdel -r alice

# Remove group
# sudo groupdel developers

# ==========================================
# PART 10: Advanced - ACL (Like Windows NTFS)
# ==========================================

# Check if ACL is supported
sudo tune2fs -l /dev/xvda1 2>/dev/null | grep "Default mount options" || echo "Check your device"

# Set ACL - Give eve read access to dev folder
sudo setfacl -m u:eve:r /teams/dev 2>/dev/null || echo "ACL not installed (sudo apt install acl)"

# View ACL
getfacl /teams/dev 2>/dev/null

# Remove ACL
# sudo setfacl -x u:eve /teams/dev
```

---

## 3. File Permissions & Ownership

### Theory

Every file/directory has:
```
-rwxrwxrwx
│││││││││└─ Others permissions
││││││└┴┴── Group permissions  
│││└┴┴──── Owner permissions
│└───────── File type (- = file, d = directory, l = link)
```

**Permission Bits:**
```
r = read    (4)
w = write   (2)
x = execute (1)
```

**Examples:**
```
755 = rwxr-xr-x  (Owner: all, Group: read+execute, Others: read+execute)
644 = rw-r--r--  (Owner: read+write, Group: read, Others: read)
600 = rw-------  (Owner: read+write, Group: none, Others: none)
777 = rwxrwxrwx  (Everyone: all permissions - DANGEROUS!)
```

### Hands-On Exercise 4: Permissions Lab

```bash
# Create test directory
mkdir -p ~/permission-lab
cd ~/permission-lab

# ==========================================
# PART 1: Basic Permissions
# ==========================================

# Create files
touch public.txt
touch private.txt
touch script.sh

# Check default permissions
ls -l

# Change file permissions
chmod 644 public.txt   # Read for all, write for owner
chmod 600 private.txt  # Only owner can read/write
chmod 755 script.sh    # Everyone can execute

# Verify
ls -l

# ==========================================
# PART 2: Directory Permissions
# ==========================================

mkdir public_folder
mkdir private_folder
mkdir shared_folder

# Directory permissions are different:
# r = can list files (ls)
# w = can create/delete files
# x = can enter directory (cd)

chmod 755 public_folder   # Everyone can list and enter
chmod 700 private_folder  # Only owner can access
chmod 770 shared_folder   # Owner and group can access

ls -ld */

# ==========================================
# PART 3: Symbolic Permissions
# ==========================================

# Using symbols instead of numbers
chmod u+x script.sh       # User: add execute
chmod g+w shared_folder   # Group: add write
chmod o-r private.txt     # Others: remove read

# Multiple changes
chmod u+rw,g+r,o-rwx private.txt

# ==========================================
# PART 4: Ownership
# ==========================================

# Change owner
sudo chown alice:developers shared_folder

# Change only owner
sudo chown bob public.txt

# Change only group
sudo chgrp developers public_folder

# Recursive ownership
sudo chown -R alice:developers shared_folder/

# ==========================================
# PART 5: Special Permissions
# ==========================================

# SUID (Set User ID) - run as owner
chmod 4755 script.sh  # Creates: -rwsr-xr-x

# SGID (Set Group ID) - files inherit group
chmod 2755 shared_folder  # Creates: drwxr-sr-x

# Sticky Bit - only owner can delete
chmod 1777 /tmp  # Creates: drwxrwxrwt
# Example: /tmp has sticky bit

# View special permissions
ls -ld script.sh shared_folder /tmp

# ==========================================
# PART 6: umask (Default Permissions)
# ==========================================

# Check current umask
umask

# Default file: 666 - umask
# Default directory: 777 - umask

# Set umask (temporary)
umask 022  # Files: 644, Directories: 755

# Create file and check
touch test_umask.txt
ls -l test_umask.txt

# ==========================================
# PART 7: Find Files by Permissions
# ==========================================

# Find world-writable files (security risk!)
sudo find /tmp -type f -perm -002 2>/dev/null | head -5

# Find SUID files (potential security issue)
sudo find / -perm -4000 -type f 2>/dev/null | head -10

# Find files owned by specific user
find /home -user alice 2>/dev/null | head -5

# Find files with specific permissions
find . -type f -perm 644

# ==========================================
# PART 8: Common Permission Patterns
# ==========================================

# Web application files
sudo chmod 644 /var/www/html/*.html
sudo chmod 755 /var/www/html

# Script files
chmod 755 *.sh

# Config files with passwords
chmod 600 ~/.ssh/id_rsa
chmod 600 /etc/myapp/.env

# Logs (append only for group)
chmod 664 /var/log/myapp/app.log

# Docker socket (docker group access)
ls -l /var/run/docker.sock
```

---

## 4. Process Management

### Theory

**Process**: Running instance of a program
- Has PID (Process ID)
- Has parent process (PPID)
- Uses CPU, memory, files
- Can be in different states

**Process States:**
```
R - Running
S - Sleeping (waiting for event)
D - Uninterruptible sleep (usually I/O)
Z - Zombie (finished but not cleaned)
T - Stopped
```

**Process Hierarchy:**
```
systemd (PID 1)
├── sshd
│   └── bash
│       └── your_app
└── docker
    └── containers
```

### Hands-On Exercise 5: Process Management

```bash
# ==========================================
# PART 1: Viewing Processes
# ==========================================

# All processes
ps aux

# Process tree
ps auxf
pstree

# Processes for current user
ps u

# Specific process
ps aux | grep docker

# Real-time view
top
# Press 'q' to quit
# Press 'k' to kill a process
# Press '1' to show all CPUs

# Better than top
htop  # sudo apt install htop

# ==========================================
# PART 2: Process Information
# ==========================================

# Get PID by name
pgrep docker
pidof dockerd

# Detailed process info
ps -p 1 -f  # Check systemd
ps -p $$ -f  # Check current shell

# Process details from /proc
cat /proc/1/status | head -20
cat /proc/cpuinfo | grep "model name" | head -1
cat /proc/meminfo | grep MemTotal

# ==========================================
# PART 3: Starting Processes
# ==========================================

# Run in background
sleep 300 &

# Multiple background jobs
sleep 100 &
sleep 200 &
sleep 300 &

# List background jobs
jobs

# Bring to foreground
fg %1

# Send to background (Ctrl+Z, then:)
bg %1

# ==========================================
# PART 4: Killing Processes
# ==========================================

# Graceful stop (SIGTERM)
kill <PID>

# Force kill (SIGKILL)
kill -9 <PID>

# Kill by name
pkill sleep
killall sleep

# Kill all processes by user
# sudo pkill -u alice

# ==========================================
# PART 5: Process Priority (nice)
# ==========================================

# Default priority: 0
# Range: -20 (highest) to 19 (lowest)

# Start with low priority
nice -n 19 stress --cpu 4 --timeout 10s &

# Change priority of running process
renice -n 10 -p <PID>

# View priorities
ps axo pid,ni,cmd | head -20

# ==========================================
# PART 6: System Load
# ==========================================

# Load averages (1, 5, 15 minutes)
uptime
cat /proc/loadavg

# CPU usage per process
top -b -n 1 | head -20

# Memory usage
free -h

# Disk I/O
iostat 1 3  # sudo apt install sysstat

# ==========================================
# PART 7: Finding Resource Hogs
# ==========================================

# Top CPU consumers
ps aux --sort=-pcpu | head -10

# Top memory consumers
ps aux --sort=-pmem | head -10

# Check specific process
ps aux | grep dockerd

# Process file descriptors
ls /proc/$$/fd

# Open files by process
lsof -p <PID>

# ==========================================
# PART 8: Process Signals
# ==========================================

# List all signals
kill -l

# Common signals:
# SIGTERM (15) - graceful shutdown
# SIGKILL (9) - force kill
# SIGHUP (1) - reload config
# SIGSTOP (19) - pause
# SIGCONT (18) - resume

# Send specific signal
kill -SIGHUP <PID>

# Trap signals in script
# trap "echo Caught signal" SIGINT SIGTERM
```

---

## 5. SystemD & Services

### Theory

**SystemD**: Modern init system (PID 1)
- Manages services
- Handles dependencies
- Controls boot process
- Manages system state

**Service States:**
```
loaded   - Unit file read
active   - Running
inactive - Stopped
failed   - Crashed
```

**Service Types:**
```
simple   - Main process
forking  - Forks child process
oneshot  - Runs once and exits
notify   - Sends notification when ready
```

### Hands-On Exercise 6: Service Management

```bash
# ==========================================
# PART 1: Basic Service Commands
# ==========================================

# Check service status
systemctl status docker
systemctl status ssh

# Start service
sudo systemctl start docker

# Stop service
sudo systemctl stop docker

# Restart service
sudo systemctl restart docker

# Reload config (without restart)
sudo systemctl reload nginx

# Enable (start on boot)
sudo systemctl enable docker

# Disable (don't start on boot)
sudo systemctl disable docker

# Check if enabled
systemctl is-enabled docker

# Check if active
systemctl is-active docker

# ==========================================
# PART 2: Listing Services
# ==========================================

# All services
systemctl list-units --type=service

# Running services
systemctl list-units --type=service --state=running

# Failed services
systemctl list-units --type=service --state=failed

# All unit files
systemctl list-unit-files

# ==========================================
# PART 3: Service Dependencies
# ==========================================

# What depends on this service
systemctl list-dependencies docker

# Reverse dependencies
systemctl list-dependencies --reverse docker

# ==========================================
# PART 4: Service Logs (journalctl)
# ==========================================

# View service logs
sudo journalctl -u docker

# Follow logs (like tail -f)
sudo journalctl -u docker -f

# Last 50 lines
sudo journalctl -u docker -n 50

# Since boot
sudo journalctl -b

# Since specific time
sudo journalctl --since "2025-01-01"
sudo journalctl --since "1 hour ago"

# By priority
sudo journalctl -p err

# ==========================================
# PART 5: Create Custom Service
# ==========================================

# Create a simple Node.js app
mkdir -p ~/myapp
cat > ~/myapp/server.js <<'EOF'
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200);
  res.end('Hello from SystemD service!\n');
});
server.listen(3000, () => {
  console.log('Server running on port 3000');
});
EOF

# Create systemd service file
sudo tee /etc/systemd/system/myapp.service > /dev/null <<'EOF'
[Unit]
Description=My Node.js Application
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/myapp
ExecStart=/usr/bin/node server.js
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd
sudo systemctl daemon-reload

# Start service
sudo systemctl start myapp

# Check status
systemctl status myapp

# View logs
sudo journalctl -u myapp -f

# Enable on boot
sudo systemctl enable myapp

# Test
curl localhost:3000

# ==========================================
# PART 6: System Targets (Runlevels)
# ==========================================

# Current target
systemctl get-default

# Available targets
systemctl list-units --type=target

# Common targets:
# multi-user.target - CLI mode
# graphical.target - GUI mode
# rescue.target - Single user mode

# Change default target
# sudo systemctl set-default multi-user.target

# Switch target
# sudo systemctl isolate multi-user.target

# ==========================================
# PART 7: System Control
# ==========================================

# Reboot
sudo systemctl reboot

# Poweroff
sudo systemctl poweroff

# Suspend
sudo systemctl suspend

# Hibernate
sudo systemctl hibernate

# Check system boot time
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain

# ==========================================
# PART 8: Timers (Cron alternative)
# ==========================================

# List timers
systemctl list-timers

# Create timer for backup
sudo tee /etc/systemd/system/backup.service > /dev/null <<'EOF'
[Unit]
Description=Daily Backup

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
EOF

sudo tee /etc/systemd/system/backup.timer > /dev/null <<'EOF'
[Unit]
Description=Daily Backup Timer

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
EOF

# Enable timer
sudo systemctl enable backup.timer
sudo systemctl start backup.timer

# Check timer status
systemctl list-timers backup.timer
```

---

## 6. Networking Fundamentals

### Theory

**Network Layers:**
```
Layer 7: Application (HTTP, FTP, SSH)
Layer 4: Transport (TCP, UDP)
Layer 3: Network (IP)
Layer 2: Data Link (Ethernet)
Layer 1: Physical
```

**Important Ports:**
```
22   - SSH
80   - HTTP
443  - HTTPS
3306 - MySQL
5432 - PostgreSQL
6379 - Redis
27017 - MongoDB
```

### Hands-On Exercise 7: Networking Commands

```bash
# ==========================================
# PART 1: Network Interface Information
# ==========================================

# Show all interfaces (modern)
ip addr show
ip a

# Show all interfaces (legacy)
ifconfig

# Show only IPv4
ip -4 addr

# Show specific interface
ip addr show eth0

# ==========================================
# PART 2: Routing
# ==========================================

# Show routing table
ip route show

# Default gateway
ip route | grep default

# Add route
# sudo ip route add 192.168.1.0/24 via 10.0.0.1

# Delete route
# sudo ip route del 192.168.1.0/24

# ==========================================
# PART 3: DNS
# ==========================================

# DNS lookup
nslookup google.com
dig google.com
host google.com

# Reverse DNS
dig -x 8.8.8.8

# Check DNS servers
cat /etc/resolv.conf

# Test DNS resolution
getent hosts google.com

# ==========================================
# PART 4: Connectivity Testing
# ==========================================

# Ping test
ping -c 4 google.com

# Traceroute
traceroute google.com
mtr google.com  # Better than traceroute

# Test specific port
nc -zv google.com 443
telnet google.com 80

# ==========================================
# PART 5: Network Statistics
# ==========================================

# Network connections
netstat -tuln  # All listening TCP/UDP
ss -tuln       # Modern alternative

# Active connections
netstat -tunp
ss -tunp

# Socket statistics
ss -s

# ==========================================
# PART 6: Firewall (UFW)
# ==========================================

# Check firewall status
sudo ufw status

# Enable firewall
sudo ufw enable

# Allow SSH
sudo ufw allow 22/tcp
sudo ufw allow ssh

# Allow HTTP/HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Allow specific port range
sudo ufw allow 8000:8100/tcp

# Allow from specific IP
sudo ufw allow from 192.168.1.100

# Deny traffic
sudo ufw deny 23/tcp

# Delete rule
sudo ufw delete allow 80/tcp

# Reset firewall
# sudo ufw reset

# ==========================================
# PART 7: Network Traffic Analysis
# ==========================================

# Capture packets (requires root)
sudo tcpdump -i eth0 -c 10
sudo tcpdump -i any port 80

# Monitor bandwidth
iftop  # sudo apt install iftop
nethogs  # sudo apt install nethogs

# Network usage
vnstat -l  # sudo apt install vnstat

# ==========================================
# PART 8: Testing Web Services
# ==========================================

# HTTP request
curl https://api.github.com

# With headers
curl -I https://google.com

# POST request
curl -X POST -d "key=value" https://httpbin.org/post

# Download file
wget https://example.com/file.txt

# Speed test
curl -o /dev/null https://speed.cloudflare.com/__down?bytes=100000000

# ==========================================
# PART 9: Network Configuration Files
# ==========================================

# View network config
cat /etc/netplan/*.yaml

# Hosts file
cat /etc/hosts

# Add custom host
echo "127.0.0.1 myapp.local" | sudo tee -a /etc/hosts

# Test
ping myapp.local

# ==========================================
# PART 10: Debugging Network Issues
# ==========================================

# Check if service is listening
sudo ss -tlnp | grep :80

# Test local port
curl localhost:8080

# Check network interface stats
ip -s link

# Network performance
iperf3 -s  # Server mode
# iperf3 -c <server-ip>  # Client mode
```

---

## 7. Docker & Containers

### Theory

**Container**: Isolated process using Linux namespaces and cgroups
- **Not a VM** - shares host kernel
- Isolated: filesystem, network, processes
- Lightweight and fast

**Docker Components:**
```
Docker Daemon - Background service
Docker Client - CLI tool
Images - Read-only templates
Containers - Running instances
Volumes - Persistent storage
Networks - Container networking
```

### Hands-On Exercise 8: Docker Deep Dive

```bash
# ==========================================
# PART 1: Docker Installation Check
# ==========================================

# Version info
docker --version
docker version
docker info

# Test Docker
docker run hello-world

# ==========================================
# PART 2: Container Basics
# ==========================================

# Run container (foreground)
docker run ubuntu echo "Hello Docker"

# Run interactive container
docker run -it ubuntu bash
# Inside container:
ls
whoami
ps aux
exit

# Run in background (detached)
docker run -d nginx

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# ==========================================
# PART 3: Container Management
# ==========================================

# Start stopped container
docker start <container_id>

# Stop container
docker stop <container_id>

# Restart container
docker restart <container_id>

# Remove container
docker rm <container_id>

# Force remove running container
docker rm -f <container_id>

# Remove all stopped containers
docker container prune

# ==========================================
# PART 4: Working with Images
# ==========================================

# List images
docker images

# Pull image
docker pull nginx:alpine
docker pull node:18

# Search images
docker search postgres

# Remove image
docker rmi nginx:alpine

# Remove unused images
docker image prune

# ==========================================
# PART 5: Container Inspection
# ==========================================

# View logs
docker logs <container_id>
docker logs -f <container_id>  # Follow
docker logs --tail 50 <container_id>

# Execute command in running container
docker exec <container_id> ls -la
docker exec -it <container_id> bash

# Container stats
docker stats
docker stats <container_id>

# Inspect container
docker inspect <container_id>

# Container processes
docker top <container_id>

# ==========================================
# PART 6: Port Mapping & Volumes
# ==========================================

# Map ports
docker run -d -p 8080:80 nginx
curl localhost:8080

# Map multiple ports
docker run -d -p 8080:80 -p 8443:443 nginx

# Mount volume
docker run -d -v /host/path:/container/path nginx

# Named volume
docker volume create mydata
docker run -d -v mydata:/data ubuntu

# List volumes
docker volume ls

# ==========================================
# PART 7: Docker Networks
# ==========================================

# List networks
docker network ls

# Default networks:
# bridge - default
# host - use host network
# none - no network

# Create custom network
docker network create mynetwork

# Run container in network
docker run -d --network mynetwork --name web nginx
docker run -d --network mynetwork --name db postgres

# Inspect network
docker network inspect mynetwork

# Connect running container to network
docker network connect mynetwork <container_id>

# ==========================================
# PART 8: Building Images
# ==========================================

# Create Dockerfile
mkdir ~/docker-test
cd ~/docker-test

cat > Dockerfile <<'EOF'
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
EOF

# Create simple app
cat > server.js <<'EOF'
const http = require('http');


Important topic for DevOps

File Systems
Package management
Systemd
Persmissions
Logs
Disk and Process management


