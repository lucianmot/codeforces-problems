# Python - Soldier and Bananas
# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())
answer = 0
for x in range(1, w+1):
    answer+=k * x

print(answer-n) if answer-n > 0 else print("0")

k * (w * (w - 1)) 
