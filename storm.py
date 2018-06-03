#!/data/data/com.termux/files/usr/bin/python

from termcolor import colored
import os

def mainMenu():
    arr = ["Primary setting", "Installing Frameworks", "Installing Linux OS", "Add Repository"]
    while True:
        print(colored("+" + "---+"*11, 'cyan'))
        print(colored("  _____   _______    ____    _____    __  __  ", 'yellow'))
        print(colored(" / ____| |__   __|  / __ \  |  __ \  |  \/  | ", 'yellow'))
        print(colored("| (___      | |    | |  | | | |__) | | \  / | ", 'yellow'))
        print(colored(" \___ \     | |    | |  | | |  _  /  | |\/| | ", 'yellow'))
        print(colored(" ____) |    | |    | |__| | | | \ \  | |  | | ", 'yellow'))
        print(colored("|_____/     |_|     \____/  |_|  \_\ |_|  |_| ", 'yellow'))
        print(colored("+---"*4 + "> Main Menu <" + "---+"*4, 'cyan'))
        for i in range(len(arr)):
            print("\t[", i+1, "] --- ", arr[i], sep="")
        print("\t[99] --- Exit")
        print(colored("+---"*11 + "+", 'cyan'))
        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            firstSetting()
        elif select == "2":
            frameworks()
        elif select == "3":
            software()
        elif select == "4":
            repo()
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

def firstSetting():
    arr = ["Install Fish", "Install Zsh", "Install Sudo", "Install Useful Scripts"]
    while True:
        print(colored("+---"*4 + "> StartMenu <" + "---+"*4, 'yellow'))
        for i in range(len(arr)):
            print("\t[", i+1, "] --- ", arr[i], sep="")
        print("\t[99] --- Back to Main Menu")
        print(colored("+---"*11 + "+", 'yellow'))

        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            os.system("apt install -y fish curl")
            os.system("chsh -s fish")
            os.system("curl -L https://get.oh-my.fish | fish")
            os.system("omf install bobthefish")
            print("\n" + "---"*11)
            print(colored("Fish Installed by Default", 'yellow'))
            print("---"*11)
        elif select == "2":
            os.system("apt install -y zsh curl")
            os.system("chsh -s zsh")
            os.system("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/fornwall/oh-my-zsh/etc-shells-may-not-exist/tools/install.sh)\"")
            os.system("sed 's/ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"agnoster\"/g' -i $HOME/.zshrc")
            print("\n" + "---"*11)
            print(colored("ZSH Installed by Default", 'yellow'))
            print("---"*11)
        elif select == "3":
            os.system("git clone https://github.com/st42/termux-sudo $HOME/termux-sudo")
            os.system("cat $HOME/termux-sudo/sudo > /data/data/com.termux/files/usr/bin/sudo")
            os.system("chmod 700 /data/data/com.termux/files/usr/bin/sudo")
            print("\n" + "---"*11)
            print(colored("Sudo Installed by Default", 'yellow'))
            print("---"*11)
        elif select == "4":
            os.system("mkdir $HOME/usefulScript")
            os.system("cp $HOME/Storm/data/* $HOME/usefulScript")
            print("\n" + "---"*11)
            print(colored("Scripts installed in $HOME/usefulScript", 'yellow'))
            print("---"*11)
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

def frameworks():
    arr = ["Install Metasploit", "Install Routersploit", "Install RED-HAWK", "Install ISF", "Install TermuxTool"]
    while True:
        print(colored("+---"*4 + "> Framework <" + "---+"*4, 'yellow'))
        for i in range(len(arr)):
            print("\t[", i+1, "] --- ", arr[i], sep="")
        print("\t[99] --- Back to Main Menu")
        print(colored("+---"*11 + "+", 'yellow'))

        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            os.system("apt install -y wget")
            os.system("cd $HOME && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd $HOME && bash metasploit.sh")
            print("\n" + "---"*11)
            print(colored("Metasploit Framework Installed", 'yellow'))
            print("---"*11)
        elif select == "2":
            os.system("git clone https://github.com/reverse-shell/routersploit $HOME/routersploit")
            os.system("apt install -y termux-exec python python-dev coreutils clang libclang libsodium libsodium-dev libtool libffi libffi-dev libgrpc-dev readline-dev libcrypt libcrypt-dev openssl openssl-dev")
            os.system("pip install six wheel pycparser cffi requests")
            os.system("SODIUM_INSTALL=system pip install pynacl")
            print("\n" + "---"*11)
            print(colored("Routersploit Framework Installed", 'yellow'))
            print("---"*11)
        elif select == "3":
            os.system("apt install -y php")
            os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK $HOME/RED_HAWK")
            print("\n" + "---"*11)
            print(colored("RED-HAWK Installed", 'yellow'))
            print("---"*11)
        elif select == "4":
            os.system("apt install -y python2 python2-dev")
            os.system("git clone https://github.com/dark-lbp/isf $HOME/isf")
            os.system("pip2 install requests paramiko beautifulsoup4 pysnmp python-nmap scapy")
            print("\n" + "---"*11)
            print(colored("ISF Installed", 'yellow'))
            print("---"*11)
        elif select == "5":
            os.system("apt install -y python2 python2-dev")
            os.system("git clone https://github.com/kuburan/txtool.git $HOME/txtool")
            os.system("cd txtool && python2 install.py")
            print("\n" + "---"*11)
            print(colored("TermuxTool Installed", 'yellow'))
            print("---"*11)
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

def software():
    arr = ["Install Debian", "Install Ubuntu", "Install TermuxAlpine", "Install Kali Nethunter", "Install Fedora", "Install Arch", "Install Slackware"]
    while True:
        print(colored("+---"*4 + "> LinuxMenu <" + "---+"*4, 'yellow'))
        for i in range(len(arr)):
            print("\t[", i+1, "] --- ", arr[i], sep="")
        print("\t[99] --- Back to Main Menu")
        print(colored("+---"*11 + "+", 'yellow'))

        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            os.system("apt install -y wget")
            os.system("hash -r")
            os.system("cd $HOME && wget https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux.sh")
            os.system("cd $HOME && bash debian_on_termux.sh")
            print("\n" + "---"*11)
            print(colored("Debian Installed", 'yellow'))
            print("---"*11)
        elif select == "2":
            os.system("apt install -y wget")
            os.system("cd $HOME && wget https://raw.githubusercontent.com/Neo-Oli/termux-ubuntu/master/ubuntu.sh")
            os.system("cd $HOME && bash ubuntu.sh")
            print("\n" + "---"*11)
            print(colored("Ubuntu Installed", 'yellow'))
            print("---"*11)
        elif select == "3":
            os.system("apt install -y curl")
            os.system("cd $HOME && curl -LO https://raw.githubusercontent.com/Hax4us/TermuxAlpine/master/TermuxAlpine.sh")
            os.system("cd $HOME && bash TermuxAlpine.sh")
            print("\n" + "---"*11)
            print(colored("TermuxAlpine Installed", 'yellow'))
            print("---"*11)
        elif select == "4":
            os.system("apt install -y wget")
            os.system("cd $HOME && wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter")
            os.system("cd $HOME && bash kalinethunter")
            print("\n" + "---"*11)
            print(colored("Kali Nethunter Installed", 'yellow'))
            print("---"*11)
        elif select == "5":
            os.system("apt install -y wget")
            os.system("cd $HOME && wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
            os.system("cd $HOME && bash termux-fedora.sh")
            print("\n" + "---"*11)
            print(colored("Fedora Installed", 'yellow'))
            print("---"*11)
        elif select == "6":
            os.system("apt install -y wget")
            os.system("cd $HOME && wget https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.sh")
            os.system("cd $HOME && bash setupTermuxArch.sh")
            print("\n" + "---"*11)
            print(colored("Arch Installed", 'yellow'))
            print("---"*11)
        elif select == "7":
            os.system("apt install -y wget")
            os.system("cd $HOME && wget https://raw.githubusercontent.com/gwenhael-le-moine/TermuxSlack/master/setupTermuxSlack.sh")
            os.system("cd $HOME && bash setupTermuxSlack.sh")
            print("\n" + "---"*11)
            print(colored("Slackware Installed", 'yellow'))
            print("---"*11)
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

def repo():
    arr = ["Termux root packages", "Termux tools(Hax4us repo)", "Termux X11 repository(xeffyr)", "Its-pointless Game Repo", "Termux api package"]
    while True:
        print(colored("+---"*4 + ">  Package  <" + "---+"*4, 'yellow'))
        for i in range(len(arr)):
            print("\t[", i+1, "] --- ", arr[i], sep="")
        print("\t[99] --- Back to Main Menu")
        print(colored("+---"*11 + "+", 'yellow'))

        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            os.system("apt install -y dirmngr")
            os.system("apt-key adv --keyserver pgp.mit.edu --recv A46BE53C")
            os.system("mkdir -p $PREFIX/etc/apt/sources.list.d")
            os.system("echo \"deb [trusted=yes] https://grimler.se root stable\" > $PREFIX/etc/apt/sources.list.d/termux-root.list")
            os.system("apt update")
            print("\n" + "---"*11)
            print(colored("Termux root packages Installed", 'yellow'))
            print("---"*11)
        elif select == "2":
            print("Select your Arch")
            print("1) AARCH64")
            print("2) ARMHF/ARMV7 OR ARM 32BIT DEVICE")
            select1 = input(colored("-->", 'red',))
            if select1 == "1":
                os.system("apt install -y dirmngr")
                os.system("mkdir -p $PREFIX/etc/apt/sources.list.d")
                os.system("printf \"deb [trusted=yes arch=all,aarch64] https://hax4us.github.io/termux-tools/ termux extras\" > $PREFIX/etc/apt/sources.list.d/hax4us.list")
                os.system("apt update")
                print("\n" + "---"*11)
                print(colored("Termux tools(Hax4us repo) Installed", 'yellow'))
                print("---"*11)
            elif select1 == "2":
                os.system("apt install -y dirmngr")
                os.system("mkdir -p $PREFIX/etc/apt/sources.list.d")
                os.system("printf \"deb [trusted=yes arch=all,arm] https://hax4us.github.io/termux-tools/ termux extras\" > $PREFIX/etc/apt/sources.list.d/hax4us.list")
                os.system("apt update")
                print("\n" + "---"*11)
                print(colored("Termux tools(Hax4us repo) Installed", 'yellow'))
                print("---"*11)
            else:
                print(colored("The parameter is entered incorrectly!", 'red'))
        elif select == "3":
            os.system("cd $HOME && wget https://raw.githubusercontent.com/xeffyr/termux-x-repository/master/enablerepo.sh && bash enablerepo.sh")
            print("\n" + "---"*11)
            print(colored("Termux X11 repository(xeffyr) Installed", 'yellow'))
            print("---"*11)
        elif select == "4":
            os.system("apt install -y wget")
            os.system("cd $HOME && wget https://its-pointless.github.io/setup-pointless-repo.sh && bash setup-pointless-repo.sh")
            print("\n" + "---"*11)
            print(colored("Its-pointless Game Repo Installed", 'yellow'))
            print("---"*11)
        elif select == "5":
            os.system("apt install -y make clang")
            os.system("cd $HOME && git clone https://github.com/termux/termux-api-package")
            os.system("cd $HOME/termux-api-package && make -f Makefile install")
            print("\n" + "---"*11)
            print(colored("Termux api package Installed", 'yellow'))
            print("---"*11)
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

mainMenu()