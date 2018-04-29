#!/data/data/com.termux/files/usr/bin/sh
echo " ______   _______  ______  _________ _______  _       "
echo "(  __  \ (  ____ \(  ___ \ \__   __/(  ___  )( (    /|"
echo "| (  \  )| (    \/| (   ) )   ) (   | (   ) ||  \  ( |"
echo "| |   ) || (__    | (__/ /    | |   | (___) ||   \ | |"
echo "| |   | ||  __)   |  __ (     | |   |  ___  || (\ \) |"
echo "| |   ) || (      | (  \ \    | |   | (   ) || | \   |"
echo "| (__/  )| (____/\| )___) )___) (___| )   ( || )  \  |"
echo "(______/ (_______/|/ \___/ \_______/|/     \||/    )_)"

echo "1 Debian Install"
echo "2 Install Dependence"
echo "3 Exit"
read debinstal

case $debinstal in
1)
cd $HOME
еcho 'bash $HOME/bin/enter-deb -n -p' > .bashrc
apt update
apt install git
git clone https://github.com/sp4rkie/debian-on-termux
chmod 750 $HOME/debian-on-termux
cd $HOME/debian-on-termux/
bash debian_on_termux.sh
echo -en "\033[31 Complete Install, Reboot Terminal \033[31"
;;
2)
cd $HOME
apt update -y
apt install fish python-pip python net-tools wireless-tools curl git nmap 
curl -L https://get.oh-my.fish | fish
omf install flash
omf theme flash
;;
3)
exit 0
;;
*)
echo "Choose the correct option"
;;
esac
