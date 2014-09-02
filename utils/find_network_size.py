__author__ = 'Morteza'

import sys

fp = open(sys.argv[1], 'r').read().split('\n')
size = 0

for ln in fp:
    if ln == '':
        break
    line_temp = ln.split()
    line = map(int, line_temp)

    size = max(size, line[1])

print 'network size is : ', size