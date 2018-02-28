import sys
data_map = {}
for line in open(sys.argv[1], "r"):
   data = line.split(',')
   data_map[data[0].rstrip()] = data[1].rstrip()
print(data_map)

import fileinput
for line in fileinput.input([sys.argv[2]],inplace=1):
   if line.strip() in data_map:
      print(data_map[line.strip()])
   else:
      print(line.rstrip())
