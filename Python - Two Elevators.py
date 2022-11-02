# Python - Two Elevators
# https://codeforces.com/contest/1729/problem/A

testCases = int(input())

for i in range(testCases):
    a, b, c = map(int, input().split())
    x = 0
    if b > c:
        x = b - 1
    else:
        x = c - b + c - 1
    if a - 1 <  x:
        print("1")
    elif a - 1 > x:
        print("2")
    else:
        print("3")
