#!/data/data/com.termux/files/usr/bin/bash

git clone https://github.com/Deathlive/Storm $HOME/Storm
chmod -R 700 Storm
apt install git python python-dev
pip install termcolor