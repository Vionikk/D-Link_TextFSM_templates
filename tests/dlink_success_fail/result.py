import textfsm
from pprint import pprint

output = '''
Command: create vlan test tag 2

Success.                                                          

Command: create vlan test tag 2

 The VLAN already exists. 

Fail!                                                    

'''

with open('result.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output)

print(fsm.header)
print(result)

#two lists into list of dicts:
all = list()
for i in range(len(result)):
    zip_iterator = zip(fsm.header, result[i])
    dictionary = dict(zip_iterator)
    all.append(dictionary)

pprint(all)