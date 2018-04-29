#!/data/data/com.termux/files/usr/bin/sh

echo "1 Start installation Reaver"
echo "2 Start installation Dnschef"
echo "3 Start installation Sqlmap"
echo "4 Start installation Responder"
echo "5 Start installation theHarvester"
echo "6 Start installation recon-ng"
echo "7 Start installation viSQL"
echo "8 Start installation sudo"
echo "9 Exit"
read bonus

case $bonus in
1)
cd $HOME
git clone https://github.com/Deathlive/reaver
mv $HOME/reaver-wps-fork-t6x $HOME/reaver
cd $HOME/reaver/src/
sh configure
make
echo "----------------------"
echo "End of Setup Reaver"
echo "----------------------"
;;
2)
cd $HOME
git clone https://github.com/iphelix/dnschef
pip2 install dnslib ipy
echo "----------------------"
echo "End of Setup dnschef"
echo "python2 dnschef.py"
echo "----------------------"
;;
3)
cd $HOME
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap
cd $HOME/sqlmap/
echo "----------------------"
echo "End of Setup SQLmap"
echo "----------------------"
;;
4)
cd $HOME
git clone https://github.com/SpiderLabs/Responder
cd $HOME/Responder/
echo "----------------------"
echo "End of Setup Responder"
echo "----------------------"
;;
5)
cd $HOME
git clone https://github.com/laramies/theHarvester
echo "----------------------"
echo "End of Setup theHarvester"
echo "----------------------"
;;
6)
cd $HOME
git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/recon-ng.git
cp $HOME/Storm/data/keys.db $HOME/.recon-ng/
pip2 install dicttoxml dnspython jsonrpclib lxml mechanize slowaes XlsxWriter olefile PyPDF2 flask unicodecsv
echo "----------------------"
echo "End of Setup recon-ng"
echo "----------------------"
;;
7)
cd $HOME
git clone https://github.com/blackvkng/viSQL
echo "----------------------"
echo "End of Setup viSQL"
echo "----------------------"
;;
8)
cd $HOME
git clone https://github.com/st42/termux-sudo
cd $HOME/termux-sudo
cat sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo
echo "----------------------"
echo "End of Setup sudo"
echo "----------------------"
;;
9)
exit 0
;;
*)
echo "Choose the correct option"
;;
esac

#99)
#cd $HOME
#git clone https://github.com/byt3bl33d3r/MITMf
#pkg install clang python2 python2-dev libjpeg-turbo-dev ndk-sysroot clang
#pip2 install wheel Twisted
#LDFLAGS="-L/system/lib/" 
#CFLAGS="-I/data/data/com.termux/files/usr/include/" 
#pip2 install pillow
#echo "termux-chroot, pip2 install -r requirements.txt"
#;;
