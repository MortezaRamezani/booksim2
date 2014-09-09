__author__ = 'Morteza'

import sys

fp = open(sys.argv[1], 'r').read().split('\n')
temp_time = 0

pattern = [0] * 49 * 49

for ln in fp:
    if ln == '':
        break
    line_temp = ln.split()
    line = map(int, line_temp)
    pattern[line[1]*7+line[2]] += 1
    
    
for i in range(0, 49):
  for j in range(0, 49):
    print pattern[i*7+j], ' '
  print '\n'