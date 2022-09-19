# Python - Twins
# https://codeforces.com/problemset/problem/160/A

whatever = input()

t1 = 0
coin_count = 0

coins_list = list(map(int, input().split(" ")))

coins_list.sort()
coins_list.reverse()
t2 = sum(coins_list)

for i in coins_list:
  t1+=i
  t2-=i
  coin_count+=1
  if t1 > t2:
    print(coin_count)
    break
