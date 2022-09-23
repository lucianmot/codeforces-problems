# Python - Bit++
# https://codeforces.com/problemset/problem/282/A

n_k = list(map(int, input().split(" ")))
grades = list(map(int, input().split(" ")))
answer = 0
for x in grades:
    if x >= grades[n_k[1]-1] and x > 0:
        answer+=1
print(answer)
