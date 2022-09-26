# Python - Chat room
# Rating - 1000
# https://codeforces.com/problemset/problem/58/A

word = input()
answer = "hello"
counter = 0
for x in word:
    if x == answer[counter]:
        counter+=1
    if counter > 4:
        break

print("YES") if counter > 4 else print("NO")
