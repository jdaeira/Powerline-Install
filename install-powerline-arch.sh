#! /bin/bash
set -e

# Powerline-Shell Url: https://github.com/b-ryan/powerline-shell

##################################################################################################################
# Author    : John da Eira
# Email     : jdaeira@gmail.com
##################################################################################################################

# Install and Upgrade pip 
sudo pacman -S python-pip --noconfirm --needed
sudo pip install --upgrade pip

# Install Powerline Fonts
yay -S --noconfirm powerline-fonts

# Install Powerline Shell
sudo pip install powerline-shell

# Make the Configuration Directory
mkdir -p ~/.config/powerline-shell && \
powerline-shell --generate-config > ~/.config/powerline-shell/config.json

# Add Powerline Shell Code to Bash File
sudo cat config-file >> ~/.bashrc

# Move Custom Powerline Shell Files to Configuration Folder
cp powerline-shell/* ~/.config/powerline-shell

echo "***************************************************************"
echo "****************   PowerLine Shell Installed   ****************"
echo "***************************************************************"
