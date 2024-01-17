import array
from collections import deque  # double-end queue

symbols = '12#$$&*)'
codes = [ord(symbol) for symbol in symbols] # listcomps
print(codes)

cs = tuple(ord(symbol) for symbol in symbols) # genexps
print(cs)

dq = deque(range(10), maxlen = 10)
print(dq)
dq.rotate(3)  # rotate param
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(11)
print(dq)
dq.extend([-1, -2, -3])
print(dq)
dq.extendleft([20, 30, 40])
print(dq)