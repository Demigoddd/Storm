#!/data/data/com.termux/files/usr/bin/python

from termcolor import colored
import os

def mainMenu():
    li = ["Primary setting", "Installing Frameworks", "Installing Linux OS"]
    while True:
        print(colored("+" + "---+"*11, 'cyan'))
        print(colored("  _____   _______    ____    _____    __  __  ", 'yellow'))
        print(colored(" / ____| |__   __|  / __ \  |  __ \  |  \/  | ", 'yellow'))
        print(colored("| (___      | |    | |  | | | |__) | | \  / | ", 'yellow'))
        print(colored(" \___ \     | |    | |  | | |  _  /  | |\/| | ", 'yellow'))
        print(colored(" ____) |    | |    | |__| | | | \ \  | |  | | ", 'yellow'))
        print(colored("|_____/     |_|     \____/  |_|  \_\ |_|  |_| ", 'yellow'))
        print(colored("+---"*4 + "> Main Menu <" + "---+"*4, 'cyan'))
        for i in range(len(li)):
            print("\t[", i+1, "] --- ", li[i], sep="")
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
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

def firstSetting():
    li = ["Install Fish", "Install Zsh", "Install Sudo", "Install Useful Scripts"]
    while True:
        print(colored("+---"*4 + "> StartMenu <" + "---+"*4, 'yellow'))
        for i in range(len(li)):
            print("\t[", i+1, "] --- ", li[i], sep="")
        print("\t[99] --- Back to Main Menu")
        print(colored("+---"*11 + "+", 'yellow'))

        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            os.system("apt install fish curl")
            os.system("chsh -s fish")
            os.system("curl -L https://get.oh-my.fish | fish")
            os.system("omf install bobthefish")
            print("\n" + "---"*11)
            print(colored("Fish Installed by Default", 'yellow'))
            print("---"*11)
        elif select == "2":
            os.system("apt install zsh curl")
            os.system("chsh -s zsh")
            os.system("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/fornwall/oh-my-zsh/etc-shells-may-not-exist/tools/install.sh)\"")
            os.system("sed 's/ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"agnoster\"/g' -i $HOME/.zshrc")
            print("\n" + "---"*11)
            print(colored("ZSH Installed by Default", 'yellow'))
            print("---"*11)
        elif select == "3":
            os.system("cd $HOME")
            os.system("git clone https://github.com/st42/termux-sudo")
            os.system("cd $HOME/termux-sudo")
            os.system("cat sudo > /data/data/com.termux/files/usr/bin/sudo")
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
    li = ["Install Metasploit", "Install Routersploit", "Install RED-HAWK", "Install ISF", "Install TermuxTool"]
    while True:
        print(colored("+---"*4 + "> Framework <" + "---+"*4, 'yellow'))
        for i in range(len(li)):
            print("\t[", i+1, "] --- ", li[i], sep="")
        print("\t[99] --- Back to Main Menu")
        print(colored("+---"*11 + "+", 'yellow'))

        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            os.system("cd $HOME")
            os.system("pkg install wget")
            os.system("wget https://Auxilus.github.io/metasploit.sh")
            os.system("bash metasploit.sh")
            print("\n" + "---"*11)
            print(colored("Metasploit Framework Installed", 'yellow'))
            print("---"*11)
        elif select == "2":
            os.system("cd $HOME")
            os.system("git clone https://github.com/reverse-shell/routersploit")
            os.system("apt install termux-exec python python-dev coreutils clang libclang libsodium libsodium-dev libtool libffi libffi-dev libgrpc-dev readline-dev libcrypt libcrypt-dev openssl openssl-dev")
            os.system("pip install six wheel pycparser cffi requests")
            os.system("SODIUM_INSTALL=system pip install pynacl")
            print("\n" + "---"*11)
            print(colored("Routersploit Framework Installed", 'yellow'))
            print("---"*11)
        elif select == "3":
            os.system("cd $HOME")
            os.system("apt install php")
            os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
            print("\n" + "---"*11)
            print(colored("RED-HAWK Installed", 'yellow'))
            print("---"*11)
        elif select == "4":
            os.system("cd $HOME")
            os.system("apt install python2 python2-dev")
            os.system("git clone https://github.com/dark-lbp/isf")
            os.system("pip2 install requests paramiko beautifulsoup4 pysnmp python-nmap scapy")
            print("\n" + "---"*11)
            print(colored("ISF Installed", 'yellow'))
            print("---"*11)
        elif select == "5":
            os.system("cd $HOME")
            os.system("git clone https://github.com/kuburan/txtool.git")
            os.system("cd txtool")
            os.system("apt install python2 python2-dev")
            os.system("./install.py")
            print("\n" + "---"*11)
            print(colored("TermuxTool Installed", 'yellow'))
            print("---"*11)
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

def software():
    li = ["Install Debian", "Install Ubuntu", "Install TermuxAlpine", "Install Kali Nethunter", "Install Fedora", "Install Arch", "Install Slackware"]
    while True:
        print(colored("+---"*4 + "> LinuxMenu <" + "---+"*4, 'yellow'))
        for i in range(len(li)):
            print("\t[", i+1, "] --- ", li[i], sep="")
        print("\t[99] --- Back to Main Menu")
        print(colored("+---"*11 + "+", 'yellow'))

        select = input(colored("[Select]-->", 'red', attrs=['reverse', 'blink', 'bold']))

        if select == "99":
            break
        elif select == "1":
            os.system("cd $HOME")
            os.system("pkg install wget")
            os.system("hash -r")
            os.system("wget https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux.sh")
            os.system("bash debian_on_termux.sh")
            print("\n" + "---"*11)
            print(colored("Debian Installed", 'yellow'))
            print("---"*11)
        elif select == "2":
            os.system("cd $HOME")
            os.system("pkg install wget")
            os.system("wget https://raw.githubusercontent.com/Neo-Oli/termux-ubuntu/master/ubuntu.sh")
            os.system("bash ubuntu.sh")
            print("\n" + "---"*11)
            print(colored("Ubuntu Installed", 'yellow'))
            print("---"*11)
        elif select == "3":
            os.system("cd $HOME")
            os.system("pkg install curl")
            os.system("curl -LO https://raw.githubusercontent.com/Hax4us/TermuxAlpine/master/TermuxAlpine.sh")
            os.system("bash TermuxAlpine.sh")
            print("\n" + "---"*11)
            print(colored("TermuxAlpine Installed", 'yellow'))
            print("---"*11)
        elif select == "4":
            os.system("cd $HOME")
            os.system("pkg install wget")
            os.system("wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter")
            os.system("bash kalinethunter")
            print("\n" + "---"*11)
            print(colored("Kali Nethunter Installed", 'yellow'))
            print("---"*11)
        elif select == "5":
            os.system("cd $HOME")
            os.system("pkg install wget")
            os.system("wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
            os.system("bash termux-fedora.sh")
            print("\n" + "---"*11)
            print(colored("Fedora Installed", 'yellow'))
            print("---"*11)
        elif select == "6":
            os.system("cd $HOME")
            os.system("pkg install wget")
            os.system("wget https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.sh")
            os.system("bash setupTermuxArch.sh")
            print("\n" + "---"*11)
            print(colored("Arch Installed", 'yellow'))
            print("---"*11)
        elif select == "7":
            os.system("cd $HOME")
            os.system("pkg install wget")
            os.system("wget https://raw.githubusercontent.com/gwenhael-le-moine/TermuxSlack/master/setupTermuxSlack.sh")
            os.system("bash setupTermuxSlack.sh")
            print("\n" + "---"*11)
            print(colored("Slackware Installed", 'yellow'))
            print("---"*11)
        else:
            print(colored("The parameter is entered incorrectly!", 'red'))

mainMenu()