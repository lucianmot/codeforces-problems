# Python - Football
# Rating - 1000
# https://codeforces.com/problemset/problem/43/A

from collections import Counter

n = int(input())
arr = []
for x in range(n):
    team = input()
    arr.append(team)
answer = dict(Counter(arr))
print(max(answer, key=answer.get))
