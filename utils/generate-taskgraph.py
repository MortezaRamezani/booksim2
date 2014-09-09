__author__ = 'Morteza'

import sys
import math
from random import random

alpha = 0.5
beta = 0.5
f_clk = 1500
m = 128
b = 8
time = 5000000

x = int(sys.argv[2])
y = int(sys.argv[3])
net_size = x*y

fp = open(sys.argv[1], 'r').read().split('\n')
temp_time = 0

rate = []
lamb = [0] * pow(net_size,2)
state = [1] * pow(net_size,2)

for ln in fp:
  if ln == '':
    break
  for tmp in ln.split():
    rate.append(tmp)

for idx, r in enumerate(rate):
  lamb[idx] = float(r)*1000.0/(m*b*f_clk*1.0)
  #print idx, r, lamb[idx]
  
prev_time = 0

for i in range(0, net_size):
  for j in range(0, net_size):
    if (lamb[i*net_size+j] != 0):
      print 0, i, j, 0

#exit(0)

for t in range(1, time+1):
  for i in range(0, net_size):
    for j in range(0,net_size):
      if (lamb[i*net_size+j] != 0):
        state[i*net_size+j] = (random() >= alpha) if (state[i*net_size+j]) else (random() < beta)
        if (state[i*net_size+j] and (random() < lamb[i*net_size+j])): 
          print t-prev_time, i, j, 0
          prev_time = t
