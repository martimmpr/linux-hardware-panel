# Installation Guide

## Prerequisites

### System Dependencies

#### Fedora
```bash
sudo dnf install python3 python3-pip lm_sensors kernel-tools
```

#### Ubuntu/Debian
```bash
sudo apt install python3 python3-pip lm-sensors linux-cpupower
```

#### Arch Linux
```bash
sudo pacman -S python python-pip lm_sensors cpupower
```

### Python Dependencies

Install Python packages:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install PyQt5 psutil pyqtgraph
```

## Installation

### Option 1: Install with pip (Recommended)

```bash
# Install in user mode
pip install --user .

# Or install system-wide (requires sudo)
sudo pip install .
```

### Option 2: Run directly from source

```bash
# Make executable
chmod +x hardware_panel.py

# Run with Python
python3 hardware_panel.py

# Or run directly
./hardware_panel.py
```

## GPU Support

### NVIDIA GPU
Install NVIDIA drivers and tools:
```bash
# Fedora
sudo dnf install nvidia-driver nvidia-settings

# Ubuntu
sudo apt install nvidia-driver-XXX nvidia-utils

# Arch
sudo pacman -S nvidia nvidia-utils
```

### AMD GPU
AMD GPU support is built-in through the `amdgpu` driver (already included in modern kernels).

## Permissions

Some features require root/sudo access:
- Power profile management

### Running with sudo
```bash
sudo hardware-panel
# or
sudo hwpanel
```

### Optional: Configure sudo without password

**Warning: This reduces system security. Only do this if you understand the risks.**

Create a sudoers file:
```bash
sudo visudo -f /etc/sudoers.d/hardware-panel
```

Add these lines:
```
# Allow user to run hardware-panel without password
your_username ALL=(ALL) NOPASSWD: /usr/local/bin/hardware-panel
your_username ALL=(ALL) NOPASSWD: /usr/bin/cpupower
```

Replace `your_username` with your actual username.

## Initialize Sensors

Before first run, initialize sensors:
```bash
sudo sensors-detect
```

Follow the prompts and accept the defaults.

## Troubleshooting

### "cpupower not found"
Install kernel-tools or linux-cpupower package for your distribution.

### No GPU detected
- Install appropriate GPU drivers (nvidia-smi for NVIDIA)
- For AMD, ensure amdgpu driver is loaded

### Graphs not displaying
- Ensure pyqtgraph is installed: `pip install pyqtgraph`
- Try reinstalling PyQt5: `pip install --force-reinstall PyQt5`

## Uninstall

```bash
pip uninstall hardware-panel
```

Or if installed system-wide:
```bash
sudo pip uninstall hardware-panel
```