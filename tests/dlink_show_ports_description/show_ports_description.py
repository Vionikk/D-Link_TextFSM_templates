import textfsm
from pprint import pprint

show_ports = '''
Command: show ports description

Port      State/        Settings            Connection        Address  AutoSpeed
          MDIX    Speed/Duplex/FlowCtrl Speed/Duplex/FlowCtrl Learning Downgrade
-------- -------- --------------------- --------------------- -------- ---------
1        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_1_R
2        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_1_L
3        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_2_R
4        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_2_L
5        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_3_R
6        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_3_L
7        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_4_R
8        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_4_L
9        Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_5_L
10       Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Fl_5_R
11       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description: 
12       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
13       Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled
          Auto
          Description: Wi-Fi UNIFI AC PRO
14       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
15       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description: _
16       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
17       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
18       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
19       Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
20       Enabled  Auto/Disabled         100M/Full/None        Enabled  Disabled
          Auto
          Description: Studrada_115
21   (C) Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
21   (F) Enabled  Auto/Disabled         Link Down             Enabled      -
            -
          Description:
22   (C) Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
22   (F) Enabled  Auto/Disabled         Link Down             Enabled      -
            -
          Description:
23   (C) Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description:
23   (F) Enabled  Auto/Disabled         Link Down             Enabled      -
            -
          Description:
24   (C) Enabled  Auto/Disabled         Link Down             Enabled  Disabled
          Auto
          Description: UpLink
24   (F) Enabled  Auto/Disabled         1000M/Full/None       Enabled      -
            -
          Description: UpLink


Notes:(F)indicates fiber medium and (C)indicates copper medium in a combo port

25       Enabled  Auto/Disabled         Link Down             Enabled      -
            -
          Description:
26       Enabled  Auto/Disabled         Link Down             Enabled      -
            -
          Description:


'''

with open('show_ports_description.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(show_ports)

print(fsm.header)
print(result)

#two lists into list of dicts:
all = list()
for i in range(len(result)):
    zip_iterator = zip(fsm.header, result[i])
    dictionary = dict(zip_iterator)
    all.append(dictionary)

pprint(all)