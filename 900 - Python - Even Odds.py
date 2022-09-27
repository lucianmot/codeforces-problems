# Python - Even Odds
# Rating - 900
# https://codeforces.com/problemset/problem/318/A

import math
n, k = list(map(int, input().split(" ")))

odds = []
evens = []

if k <= n / 2:
    for i in range(1, n+1, 2):
            odds.append(i)
else:
    for i in range(2, n+1, 2):
            evens.append(i)
        
if k <= n / 2:
    print(odds[k-1])
else:
    half_index = k - 1 - math.ceil(n/2)
    print(evens[half_index])
