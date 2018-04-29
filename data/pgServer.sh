#!/data/data/com.termux/files/usr/bin/sh

echo "1 Server Start"
echo "2 Server Stop"
echo "3 Exit"
read serv

case $serv in
1)
cd $HOME
pg_ctl -D ~/.msfdb -l ~/.msfdb/msfdb.log start
;;
2)
cd $HOME
pg_ctl -D ~/.msfdb -l ~/.msfdb/msfdb.log stop
;;
3)
exit 0
;;
esac