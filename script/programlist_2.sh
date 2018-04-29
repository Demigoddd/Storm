#!/data/data/com.termux/files/usr/bin/sh

echo "1 Start installation Gloom-Framework"
echo "2 Start installation Isf-Framework"
echo "3 Start installation Routerhunter"
echo "4 Start installation Sslkill"
echo "5 Start installation PenTestKit"
echo "6 Start installation RED-HAWK"
echo "7 Start installation Spaghetti"
echo "8 Start installation Datasploit"
echo "9 Exit"
read bonus

case $bonus in
1)
cd $HOME
git clone https://github.com/joshDelta/Gloom-Framework
cd $HOME/Gloom-Framework
pip2 install scapy termcolor pythonwhois requests bs4 mechanize datetime email
echo "----------------------"
echo "End of Setup Gloom-Framework"
echo "python2 gloom.py"
echo "----------------------"
;;
2)
cd $HOME
git clone https://github.com/dark-lbp/isf
mv $HOME/isf Isf-Framework
pip2 install requests paramiko beautifulsoup4 pysnmp python-nmap scapy
cd $HOME/Isf-Framework
echo "----------------------"
echo "End of Setup Isf-Framework"
echo "python2 isf.py"
echo "----------------------"
;;
3)
cd $HOME
git clone https://github.com/sh1nu11bi/Routerhunter-2.0
cd $HOME/Routerhunter-2.0
pip2 install argparse requests
echo "----------------------"
echo "End of Setup Routerhunter"
echo "python2 routerhunter.py"
echo "----------------------"
;;
4)
cd $HOME
apt install build-essential python-dev libnetfilter-queue-dev
git clone https://github.com/m4n3dw0lf/sslkill
cd $HOME/sslkill
pip2 install -r requirements.txt
sudo chmod +x sslkill.py
echo "----------------------"
echo "End of Setup Sslkill"
echo "python2 sslkill.py"
echo "----------------------"
;;
5)
cd $HOME
git clone https://github.com/maldevel/PenTestKit.git
cd $HOME/PenTestKit
pip2 install -r requirements.txt
echo "----------------------"
echo "End of Setup PenTestKit"
echo "----------------------"
;;
6)
cd $HOME
apt install php
git clone https://github.com/Tuhinshubhra/RED_HAWK
cd $HOME/RED_HAWK
echo "----------------------"
echo "End of Setup RED-HAWK"
echo "php rhawk.php"
echo "----------------------"
;;
7)
cd $HOME
git clone https://github.com/m4ll0k/Spaghetti.git
cd $HOME/Spaghetti 
pip2 install -r requirements.txt
echo "----------------------"
echo "End of Setup Spaghetti"
echo "python2 spaghetti.py"
echo "----------------------"
;;
8)
cd $HOME
git clone https://github.com/datasploit/datasploit
cd $HOME/datasploit
rm -rf config_sample.py
cp $HOME/Storm/data/config.py $HOME/datasploit/
pip2 install -r requirements.txt
echo "----------------------"
echo "End of Setup Datasploit"
echo "python2 datasploit.py"
echo "----------------------"
;;
9)
exit 0
;;
*)
echo "Choose the correct option"
;;
esac
