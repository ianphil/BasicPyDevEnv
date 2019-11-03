#!/usr/bin/env bash

echo "Configuring SSH"
sudo cp -r /root/.ssh-localhost ~ 
sudo chown -R $(id -u):$(id -g) ~/.ssh-localhost
mv ~/.ssh-localhost ~/.ssh
chmod 700 ~/.ssh
chmod 600 ~/.ssh/*

echo "Seting up Virtual Environment"
python -m venv .venv
. .venv/bin/activate

echo "Installing Python Dependencies"
sudo pip install -r requirements.txt
