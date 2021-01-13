#!/bin/bash

echo "UBUNTU POST-INSTALL SCRIPT"

echo "Updating APT..."

sudo apt-get update 

echo "Installing base packages"

sudo apt-get install --yes git git-extras python3-pip 
# ici on installe git avec les supplementation git-extras et pip 
sudo snap install discord 
#on installe discord 
sudo snap install code --classic
#on instale vsc 

clear