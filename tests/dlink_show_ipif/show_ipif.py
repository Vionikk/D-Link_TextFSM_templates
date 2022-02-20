import textfsm
from pprint import pprint

show_ipif = '''
Command: show ipif

IP Interface                : System
VLAN Name                   : Hostel_Switch_Mgmt
Interface Admin State       : Enabled
Link Status                 : LinkUp
IPv4 Address                : 10.201.99.1/24 (Manual)  Primary
Proxy ARP                   : Disabled   (Local : Disabled)
IPv4 State                  : Enabled
DHCPv6 Client State         : Disabled
IPv6 State                  : Enabled
DHCP Option12 State         : Disabled
DHCP Option12 Host Name     :


Total Entries: 1

'''

with open('show_ipif.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(show_ipif)

print(fsm.header)
print(result)

#two lists into list of dicts:
all = list()
for i in range(len(result)):
    zip_iterator = zip(fsm.header, result[i])
    dictionary = dict(zip_iterator)
    all.append(dictionary)

pprint(all)