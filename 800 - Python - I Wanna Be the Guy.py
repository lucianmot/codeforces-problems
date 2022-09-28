# Python - I Wanna Be the Guy
# Rating - 800
# https://codeforces.com/contest/469/problem/A

n = int(input())
lil_n = list(range(1, n + 1))

lil_x = list(map(int, input().split(" ")))
lil_y = list(map(int, input().split(" ")))

lil_join = lil_x + lil_y

lil_join = list(set(lil_join))

answer = 0
for i in lil_n:
    if i in lil_join:
        answer = 0
    else:
        answer = 1
        print("Oh, my keyboard!")
        break
        
if answer == 0:
    print("I become the guy.")
