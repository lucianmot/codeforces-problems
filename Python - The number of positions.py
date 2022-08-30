# Python - The number of positions
# https://codeforces.com/contest/124/problem/A

n, a, b = map(int, input().split())

if n - (a+b) > 1:
    print(n-a-(n-(a+b)-1))
else:
    print(n-a)
