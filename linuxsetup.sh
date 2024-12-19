# Remove package manager lock files (if needed)
rm /var/lib/dpkg/lock
rm /var/cache/apt/archives/lock
rm /var/lib/apt/lists/lock

# Add 32-bit architecture support
sudo dpkg --add-architecture i386

# Install Python3 on the Linux system
sudo apt install python3

# Install Python dependencies for the Linux environment
pip install colored requests pyinstaller pynput
pip3 install colored requests pyinstaller pynput

# Download the Windows Python installer
sudo wget https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe

# Install Python in the Wine environment
wine python-3.8.10.exe
wine msiexec /i python-3.8.10.exe

# Upgrade pip and install dependencies in the Wine Python environment
sudo wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/python.exe -m pip install --upgrade pip
sudo wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/python.exe -m pip install colored requests pyinstaller pynput

# Install additional GNOME Shell extension
sudo apt install -y gnome-shell-extension-dashtodock
