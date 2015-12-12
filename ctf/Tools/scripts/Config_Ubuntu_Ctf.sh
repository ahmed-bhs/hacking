#!/bin/sh
#Config Ubuntu for CTF
echo "Install Updates"
sleep 3
apt-get update -y
apt-get upgrade -y
clear sct
echo "READY!!"
sleep 3
apt-get install htop -y
sleep 3
echo "htop installed"
apt-get install vlc -y
sleep 3
echo "vlc installed"
apt-get install gimp -y
sleep 3
echo "gimp installed"
apt-get install git -y
sleep 3
echo "git installed"
apt-get install asciinema
echo "Asciinema Installed"
clear sct
echo "Install Basics OK!"
sleep 3
echo "Install CTF Tools"
apt-get install bless -y
echo "Bless Installed"
sleep 3
apt-get install ht -y
echo "Hte Installed"
sleep 3
apt-get install audacity -y
echo "Audacity Installed"
sleep 3
apt-get install pngcheck -y
echo "Pngcheck Installed"
sleep 3
apt-get install exif -y
echo "Exif Installed"
sleep 3
apt-get install steghide -y
echo "Steghide Installed"
sleep 3
apt-get install binwalk -y
echo "Binwalk Installed"
sleep 3
apt-get install pcapfix -y
echo "Pcapfix Installed"
sleep 3
apt-get install wireshark -y
echo "Wireshark Installed"
sleep 3
apt-get install foremost -y
echo "foremost Installed"
sleep 3
apt-get install ffmpeg -y
echo "Ffmpeg Installed"
sleep 3
apt-get install volatility -y
echo "Volatility Installed"
sleep 3
apt-get install ophcrack -y
echo "Ophcrack Installed"
sleep 3
apt-get install pngmeta -y
echo "Pngmeta Installed"
sleep 3
clear sct
echo "Ctf Tools READY!"
sleep 3
echo "Config Python"
apt-get install python-setuptools python-pip enscript -y
echo "Install Modules Python"
sleep 3
pip install github3.py
pip install pwntools
pip install click
pip install scapy
clear sct
echo "Python Configured"
