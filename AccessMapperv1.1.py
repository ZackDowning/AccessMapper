from pyfiglet import Figlet

Font = Figlet(font='Ogre')
Figlet = Font.renderText('AccessMapper')
print(Figlet, "          Version 1.1          \n"
                    "     Compiled by Zack Downing   \n"
                    "  ******************************\n")

import getpass

from netmiko import ConnectHandler

HOST = input("Enter Switch IP Address: ")
user = input("Enter Username: ")
PASS = getpass.getpass(prompt="Enter Password: ")
logincreds = {'device_type': 'cisco_ios',
              'ip': HOST.encode('ascii'),
              'username': user.encode('ascii'),
              'password': PASS
              }

device = ConnectHandler(**logincreds)

INT = "int " + input("Enter SwitchPort: \n"
                     "Ex: GigabitEthernet1/0/1\n"
                     "Ex: GigabitEthernet0/2")
VID = "sw ac vl " + input("Enter Vlan ID: ")

config = [INT,
          "sw mo ac",
          VID,
          "no shut",
          "do wr mem",
          "end"
          ]

device.send_config_set(config)

output1 = device.send_command("sh run " + INT)
output2 = device.send_command("sh startup-config | inc Last config")

print(output1)
print(output2)

device.disconnect()

input("Press Enter to end program.")
print("Have a nice day!\n")
