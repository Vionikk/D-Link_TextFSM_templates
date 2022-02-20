import textfsm

show_switch = '''
Command: show switch

Device Type        : DES-3028 Fast Ethernet Switch
MAC Address        : 00-21-91-92-47-B3
IP Address         : 192.168.31.235 (Manual)
VLAN Name          : default
Subnet Mask        : 255.255.255.0
Default Gateway    : 0.0.0.0
Boot PROM Version  : Build 1.00-B04
Firmware Version   : Build 2.94.B22
Hardware Version   : A1
System Name        :
System Location    :
System Uptime      : 0 days, 0 hours, 0 minutes, 56 seconds
System Contact     :
Spanning Tree      : Disabled
GVRP               : Disabled
IGMP Snooping      : Disabled
VLAN trunk         : Disabled
802.1x             : Disabled
TELNET             : Enabled(TCP  23)
WEB                : Enabled(TCP  80)
RMON               : Disabled
SSH                : Enabled(TCP  22)
SSL                : Disabled
Clipaging          : Disabled
Syslog Global State: Disabled
Dual Image         : Supported
Password Encryption Status : Disabled
'''

with open('show_switch.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(show_switch)

print(fsm.header)
print(result)

#two lists to dict:
zip_iterator = zip(fsm.header, result[0])
dictionary = dict(zip_iterator)
print(dictionary)
