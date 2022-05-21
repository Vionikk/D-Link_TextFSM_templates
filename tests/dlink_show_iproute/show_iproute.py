import textfsm
from pprint import pprint

show_arpentry = '''
Command: show iproute


Routing Table

IP Address/Netmask  Gateway          Interface    Hops     Protocol
------------------  ---------------  -----------  -------  --------
192.168.31.0/24     0.0.0.0          System       1        Local

Total Entries  : 1

'''

with open('show_iproute.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(show_arpentry)

print(fsm.header)
print(result)

#two lists into list of dicts:
all = list()
for i in range(len(result)):
    zip_iterator = zip(fsm.header, result[i])
    dictionary = dict(zip_iterator)
    all.append(dictionary)

pprint(all)