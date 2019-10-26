from InitVMs import SW_Installer

def printMenu():
    print("1.Display IPs of Internal Network.\n\
2.Choose VM for Installation\n\
3.Quit SW Installer\n")


def enter_ip():
    ip_input = False
    while not ip_input:
        ip_str = input("Enter IP address for Installation:")
        ip_parse_str = str(ip_str)
        octets_list = ip_parse_str.split(".")
        if len(octets_list) != 4:
            print("IP address  - Wrong Format  -  Should contain 4 octets")
            continue
        for i in range(4):
            octet_as_num = int(octets_list[i])
            if octet_as_num < 0 or octet_as_num > 255:
                print("Aborting - octets value should be between 0 and 255")
                break
            else:
                if i == 3:
                    ip_input = True
    return ip_str

def startInstallerMenu():
    installer = SW_Installer.Installer()
    while True:
        printMenu()
        choice = input("Enter your choice:")
        if choice == '1':
            installer.display_ips()
        elif choice == '2':
            ip = enter_ip()
            installer.install_sw(ip)
        elif choice == '3':
            print("Quit Installer.")
            break;
        else:
            raise IndexError(choice)

if __name__ == '__main__':
    startInstallerMenu()
