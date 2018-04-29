#!/data/data/com.termux/files/usr/bin/sh

echo "1 Start installation Metasploit Framework"
echo "2 Correct mistakes datax and PREFIX"
echo "3 Create a database for MSF"
echo "4 Exit"
read msfgo

case $msfgo in
1)
cd $HOME
apt update
apt upgrade
pkg install autoconf bison clang coreutils curl findutils git apr apr-util libffi-dev libgmp-dev libpcap-dev \
    postgresql-dev readline-dev libsqlite-dev openssl-dev libtool libxml2-dev libxslt-dev ncurses-dev pkg-config \
    postgresql-contrib wget make ruby-dev libgrpc-dev termux-tools ncurses ncurses-utils libsodium libsodium-dev termux-exec
echo "Dependencies Installed"
git clone https://github.com/rapid7/metasploit-framework --depth 1
#sed 's/nokogiri (1.8.0)/nokogiri (1.8.1)/g' -i $HOME/metasploit-framework/Gemfile.lock
cd $HOME/metasploit-framework/
gem install bundler
gem install nokogiri -- --use-system-libraries

echo "Install GRPC"
cd $HOME/metasploit-framework/
sed 's|grpc (.*|grpc (1.4.1)|g' -i Gemfile.lock
gem unpack grpc -v 1.4.1
cd $HOME/metasploit-framework/grpc-1.4.1/
curl -LO https://raw.githubusercontent.com/grpc/grpc/v1.4.1/grpc.gemspec
curl -L https://wiki.termux.com/images/b/bf/Grpc_extconf.patch -o extconf.patch
patch -p1 < extconf.patch
gem build grpc.gemspec
gem install grpc-1.4.1.gem
cd ..
rm -rf grpc-1.4.1

gem install bundler --pre

echo "Install GEM"
cd $HOME/metasploit-framework
bundle install

cd $HOME
mv $HOME/metasploit-framework $HOME/msfconsole
echo "-------------------------------"
echo "use termux-chroot and install = gem install rbnacl-libsodium =, Start the option-2"
echo "-------------------------------"
;;
2)
echo "Correct mistakes datax and Shebang-PREFIX"
cd $HOME
apt install -y termux-elf-cleaner
termux-elf-cleaner /data/data/com.termux/files/usr/lib/ruby/gems/2.4.0/gems/pg-0.20.0/lib/pg_ext.so
echo "Datax error fixed"

echo "Performance shebang fix"
cd $HOME/msfconsole
$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{\} \;
echo "Installation completed"

ln -s $HOME/msfconsole/msfconsole /data/data/com.termux/files/usr/bin/

rm -rf $HOME/msfconsole/modules/auxiliary/gather/http_pdf_authors.rb
echo "run msfconsole"
;;
3)
echo "Create a database"
cd $HOME
cp $HOME/Storm/data/database.yml $HOME/msfconsole/config

cd $HOME
mkdir ~/.msfdb
initdb ~/.msfdb
pg_ctl -D ~/.msfdb -l ~/.msfdb/msfdb.log start

echo "-------------------------------"
echo "createuser msf"
echo "createdb msfdb"
echo "-------------------------------"
echo "pg_ctl -D ~/.msfdb -l ~/.msfdb/msfdb.log stop"
echo "-------------------------------"
;;
4)
exit 0
;;
*)
echo "Choose the correct option"
;;
esac
