import textfsm
from pprint import pprint

show_ports = '''
Command: show ports

Port      State/        Settings            Connection        Address  AutoSpeed
          MDIX    Speed/Duplex/FlowCtrl Speed/Duplex/FlowCtrl Learning Downgrade
-------- -------- --------------------- --------------------- -------- ---------
1        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
2        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
3        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
4        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
5        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
6        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
7        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
8        Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
9        Enabled  Auto/Disabled         100M/Full/None        Enabled  Disabled 
          Auto  
                                                                                
10       Disabled Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
11       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
12       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
13       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
14       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
15       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
16       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
17       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
18       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
                                                                                
19       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
20       Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
21   (C) Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
21   (F) Enabled  Auto/Disabled         Link Down             Enabled      -    
            -    
22   (C) Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
22   (F) Enabled  Auto/Disabled         Link Down             Enabled      -    
            -    
23   (C) Enabled  Auto/Disabled         Link Down             Enabled  Disabled 
          Auto  
23   (F) Enabled  Auto/Disabled         Link Down             Enabled      -    
            -    
                                                                                
                                                                                
Notes:(F)indicates fiber medium and (C)indicates copper medium in a combo port
24   (C) Enabled  Auto/Disabled         1000M/Full/None       Enabled  Disabled 
          Auto  
24   (F) Enabled  Auto/Disabled         Link Down             Enabled      -    
            -    
25       Enabled  Auto/Disabled         Link Down             Enabled           
            -    
26       Enabled  Auto/Disabled         Link Down             Enabled           
            -    
                                                                                
                                          

'''

with open('show_ports.template') as template:
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