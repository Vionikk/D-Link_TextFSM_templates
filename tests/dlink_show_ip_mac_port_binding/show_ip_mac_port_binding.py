import textfsm
from pprint import pprint

show_ip_mac_port_binding = '''
Command: show address_binding dhcp_snoop binding_entry

 S (Status) - A: Active, I: Inactive
 Time - Left Time (sec)

 IP Address                              MAC Address       S  LT(sec)    Port
 --------------------------------------- ----------------- -- ---------- -----
 10.201.2.30                             7C-8B-CA-7F-C5-A3 A  790881     3
 10.201.2.60                             00-1F-1F-B1-FB-D1 A  790392     6
 10.201.2.70                             18-A6-F7-FC-C3-61 A  842134     7
 10.201.2.90                             28-D1-27-0A-EF-69 A  757786     9
 10.201.2.100                            18-D6-C7-A2-27-15 A  331085     10
 10.201.2.110                            50-64-2B-64-33-36 A  763098     11
 10.201.2.130                            8C-DE-F9-C8-46-BC A  408278     13
 10.201.2.140                            04-5E-A4-7B-2B-19 A  616341     14
 10.201.2.150                            60-A4-B7-BB-3A-DA A  246891     15
 10.201.2.160                            B0-6E-BF-78-D3-28 A  175049     16
 10.201.2.170                            0C-80-63-C0-60-81 A  763153     17
 10.201.2.190                            B0-BE-76-67-16-AF A  763153     19
 10.201.2.200                            18-D6-C7-A6-25-49 A  851064     20
 10.201.2.210                            08-55-31-E3-43-2D A  357629     21
 10.201.2.220                            C0-A5-DD-1F-14-42 A  328627     22
 10.201.2.230                            88-C3-97-E8-51-08 A  763353     23

Total Entries : 16

'''

with open('show_ip_mac_port_binding.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(show_ip_mac_port_binding)

print(fsm.header)
print(result)

#two lists into list of dicts:
all = list()
for i in range(len(result)):
    zip_iterator = zip(fsm.header, result[i])
    dictionary = dict(zip_iterator)
    all.append(dictionary)

pprint(all)

print()
for i in range(len(all)):
    print(all[i]['Port'] + '   ' + all[i]['IP_Address'] + '   ' +  all[i]['MAC_Address'])