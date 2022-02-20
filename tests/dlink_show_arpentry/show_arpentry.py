import textfsm
from pprint import pprint

show_arpentry = '''
 ARP Aging Time : 20

Interface      IP Address       MAC Address        Type
-------------  ---------------  -----------------  ---------------
System         192.168.173.0    FF-FF-FF-FF-FF-FF  Local/Broadcast
System         192.168.173.1    00-01-21-01-52-96  Dynamic
System         192.168.173.2    00-AD-24-83-95-F8  Local
System         192.168.173.255  FF-FF-FF-FF-FF-FF  Local/Broadcast

Total Entries: 4

'''

with open('show_arpentry.template') as template:
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