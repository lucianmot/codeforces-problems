# Python - Lucky?
# Rating - 800
# https://codeforces.com/problemset/problem/1676/A

testCases = int(input())

for i in range(testCases):
    s = list(map(int, str(input())))

    print("YES") if s[0] + s[1] + s[2] == s[3] + s[4] + s[5] else print("NO")
