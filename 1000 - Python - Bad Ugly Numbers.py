# Python - Bad Ugly Numbers
# https://codeforces.com/contest/1326/problem/A

testCases = int(input())

for x in range(testCases):
    n = int(input())
    if n == 1:
        print("-1")
    else:
        startNumber = "2"+((n-1) * "3")
        print(startNumber)
