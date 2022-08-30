# Python - Elephant
# https://codeforces.com/contest/617/problem/A

distance = int(input())

if distance % 5 == 0:
    print(int(distance/5))
else:
    print(int(distance/5)+1)
