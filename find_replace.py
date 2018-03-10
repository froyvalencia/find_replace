import sys
data_map = {}
for line in open(sys.argv[1], "r"):
   data = line.split(',')
   data_map[data[0].rstrip()] = data[1].rstrip()
'''
print(data_map)
a = data_map.keys()
a.sort()

count = 1
for l in a:
   print(str(count) + ' ' + l)
   count +=1
'''

import fileinput
s = '      ' 
for line in fileinput.input([sys.argv[2]],inplace=1):
   if line.strip() in data_map:
      print(s + data_map[line.strip()])
   else:
      print(line.rstrip())
