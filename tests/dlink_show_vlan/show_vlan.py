import textfsm
from pprint import pprint

show_vlan = '''
Command: show vlan


VLAN Trunk State        : Disabled
VLAN Trunk Member Ports :


VID             : 1           VLAN Name       : default
VLAN Type       : Static      Advertisement   : Enabled
Member Ports    : 1-28
Static Ports    : 1-28
Current Tagged Ports   :
Current Untagged Ports : 1-28
Static Tagged Ports    :
Static Untagged Ports  : 1-28
Forbidden Ports        :

VID             : 12          VLAN Name       : test
VLAN Type       : Static      Advertisement   : Disabled
Member Ports    : 2
Static Ports    : 2
Current Tagged Ports   : 2
Current Untagged Ports :
Static Tagged Ports    : 2
Static Untagged Ports  :
Forbidden Ports        :

VID             : 24          VLAN Name       : lox
VLAN Type       : Static      Advertisement   : Disabled
Member Ports    : 3-4
Static Ports    : 3-4
Current Tagged Ports   : 3-4
Current Untagged Ports :
Static Tagged Ports    : 3-4
Static Untagged Ports  :
Forbidden Ports        :

Total Entries  : 2

'''

with open('show_vlan.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(show_vlan)

#print(fsm.header)
#print(result)

#two lists into list of dicts:
all = list()
for i in range(len(result)):
    zip_iterator = zip(fsm.header, result[i])
    dictionary = dict(zip_iterator)
    all.append(dictionary)

pprint(all)