import textfsm
from pprint import pprint

show_arpentry = '''
Command: show fdb

Unicast MAC Address Aging Time  = 300

VID  VLAN Name                        MAC Address       Port Type
---- -------------------------------- ----------------- ---- ---------------
1    default                          00-21-91-92-47-B3 CPU  Self
1    default                          18-31-BF-96-59-11 26   Dynamic
1    default                          6A-69-EC-D4-47-E2 26   Dynamic
1    default                          6A-B7-5F-7A-78-1E 26   Dynamic
1    default                          88-C3-97-ED-21-9D 26   Dynamic
1    default                          D8-F2-CA-BD-30-A8 26   Dynamic

Total Entries  : 6

'''

with open('show_fdb.template') as template:
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