# Python - Nearly Lucky Number
# Rating - 800
# https://codeforces.com/contest/110/problem/A

n = str(input())

nearLuckyN = n.count("4") + n.count("7")

if nearLuckyN == 4 or nearLuckyN == 7:
    print("YES")
else:
    print("NO")
