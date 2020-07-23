from pyfiglet import Figlet

Font = Figlet(font='Ogre')
Figlet = Font.renderText('AccessMapper')
print(Figlet, "          Version 1.1          \n"
                    "     Compiled by Zack Downing   \n"
                    "  ******************************\n")

import getpass

from netmiko import ConnectHandler

HOST = input("Enter Switch IP Address: ")
print("")
user = input("Enter Username: ")
print("")
PASS = getpass.getpass(prompt="Enter Password: ")
print("")
logincreds = {'device_type': 'cisco_ios',
              'ip': HOST.encode('ascii'),
              'username': user.encode('ascii'),
              'password': PASS
              }

device = ConnectHandler(**logincreds)

INT = "int " + input("Enter SwitchPort: \n"
                     "\n"
                     "Ex: GigabitEthernet1/0/1\n"
                     "Ex: GigabitEthernet0/2\n"
                     "\n"
                     "SwitchPort: ")
print("")
VID = "sw ac vl " + input("Enter Vlan ID: ")
print("")
config = [INT,
          "sw mo ac",
          VID,
          "no shut",
          "do wr mem",
          "end"
          ]

device.send_config_set(config)

output = device.send_command("sh startup-config | inc NVRAM")

print(output + "\n")

device.disconnect()

input("Press Enter to end program.")
print("")
print("Have a nice day!")
