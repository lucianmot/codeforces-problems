# Python - Jzzhu and Children
# https://codeforces.com/contest/450/problem/A  

import math;
 
n, m = list(map(int, input().split(" ")));
c = list(map(int, input().split(" ")));
 
max = -1;
r = -1;
 
for i, v in enumerate(c):
  x = math.ceil(v / m);
  
  if x >= max:
    max = x;
    r = i+1;
 
print (r);
