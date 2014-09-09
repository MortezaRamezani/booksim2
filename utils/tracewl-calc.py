__author__ = 'Morteza'

import sys

fp = open(sys.argv[1], 'r').read().split('\n')
temp_time = 0
total_time = 0

for ln in fp:
    if ln == '':
        break
    line_temp = ln.split()
    line = map(int, line_temp)
    total_time += line[0]
    
print total_time