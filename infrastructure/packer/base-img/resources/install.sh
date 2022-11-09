#!/bin/bash
set -e

# Install Python 3.8.12
sudo apt-get update && sudo apt-get -y upgrade

sudo apt-get install -y build-essential checkinstall > /dev/null 2>&1
sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev > /dev/null 2>&1

cd /opt
sudo wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz > /dev/null 2>&1
sudo tar xzf Python-3.8.12.tgz > /dev/null 2>&1

cd Python-3.8.12
sudo ./configure --enable-optimizations > /dev/null 2>&1
sudo make altinstall > /dev/null 2>&1

cd /opt
sudo rm -f Python-3.8.12.tgz

# Install pip
python3.8 -m ensurepip --upgrade > /dev/null 2>&1
python3.8 -m pip install --upgrade pip > /dev/null 2>&1

# Create directory structure
mkdir /apps
chmod 777 /apps