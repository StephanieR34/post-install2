import os

os.system("echo 'UBUNTU POST-INSTALL SCRIPT'")

os.system("echo "Updating APT...")

oc.system("sudo apt-get update")

oc.system("echo "Installing base packages")

oc.system("sudo apt-get install --yes git git-extras python3-pip)
# ici on installe git avec les supplementation git-extras et pip 
oc.system("sudo snap install discord")
#on installe discord 
oc.system("sudo snap install code --classic")
#on instale vsc 

