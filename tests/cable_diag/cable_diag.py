import textfsm
from pprint import pprint

cable_diag = '''
Command: cable_diag ports all

Perform Cable Diagnostics ...

Port      Type      Link Status    Test Result                 Cable Length (M)
------  ----------  -------------  -------------------------  -----------------
1       100BASE-T   Link Down      Pair 2 Open      at  44M          -
                                   Pair 3 Open      at  45M
2       100BASE-T   Link Up        OK                                66
7       100BASE-T   Link Down      No Cable                          -
25      1000BASE-T      -              -                             -

'''

cable_diag_2 = '''
Command: cable_diag ports all

Perform Cable Diagnostics ...

Port      Type      Link Status    Test Result                 Cable Length (M)
------  ----------  -------------  -------------------------  -----------------
1       100BASE-T   Link Down      Pair 2 Open      at  44M          -
                                   Pair 3 Open      at  45M
2       100BASE-T   Link Up        OK                                66
3       100BASE-T   Link Down      Pair 2 Open      at  45M          -
                                   Pair 3 Open      at  45M
4       100BASE-T   Link Down      Pair 2 Open      at  46M          -
                                   Pair 3 Open      at  45M
5       100BASE-T   Link Up        OK                                87
6       100BASE-T   Link Down      Pair 2 Open      at  42M          -
                                   Pair 3 Open      at  42M
7       100BASE-T   Link Down      No Cable                          -
8       100BASE-T   Link Down      Pair 2 Open      at  42M          -
                                   Pair 3 Open      at  42M
9       100BASE-T   Link Up        OK                                66
10      100BASE-T   Link Up        OK                                78
11      100BASE-T   Link Down      Pair 2 Open      at  34M          -
                                   Pair 3 Open      at  34M
12      100BASE-T   Link Down      Pair 2 Open      at  40M          -
                                   Pair 3 Open      at  40M
13      100BASE-T   Link Up        OK                                59
14      100BASE-T   Link Up        OK                                63
15      100BASE-T   Link Up        OK                                59
16      100BASE-T   Link Up        OK                                56
17      100BASE-T   Link Up        OK                                41
18      100BASE-T   Link Down      Pair 2 Open      at  23M          -
                                   Pair 3 Open      at  23M
19      100BASE-T   Link Up        OK                                35
20      100BASE-T   Link Down      No Cable                          -
21      100BASE-T   Link Up        OK                                38
22      100BASE-T   Link Up        OK                                29
23      100BASE-T   Link Up        OK                                29
24      100BASE-T   Link Up        OK                                38
25      1000BASE-T      -              -                             -
26      1000BASE-T      -              -                             -
27      1000BASE-X      -              -                             -
28      1000BASE-X      -              -                             -

'''

with open('cable_diag.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(cable_diag)

print(fsm.header)
print(result)

#two lists into list of dicts:
all = list()
for i in range(len(result)):
    zip_iterator = zip(fsm.header, result[i])
    dictionary = dict(zip_iterator)
    all.append(dictionary)

pprint(all)