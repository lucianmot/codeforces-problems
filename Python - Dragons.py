# Python - Dragons
# https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
answer=0
fight = []

for i in range(n):
    x, y = map(int, input().split())
    fight.append([x, y])

fight = sorted(fight, key=lambda x: x[0])

for x in fight:
    if s > x[0]:
        s+=x[1]
    else:
        answer+=1

print("YES") if answer==0 else print("NO")
