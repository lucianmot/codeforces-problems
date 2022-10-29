# Python - Soldier and Bananas
# https://codeforces.com/problemset/problem/546/A  

# 1st solution
k, n, w = map(int, input().split())
answer = 0
for x in range(1, w+1):
    answer+=k * x

print(answer-n) if answer-n > 0 else print("0")

k * (w * (w - 1))

# 2nd solution
k, n, w = map(int, input().split());

s = w * (w+1) / 2 * k - n;

print (int(s)) if s > 0 else print (0);
