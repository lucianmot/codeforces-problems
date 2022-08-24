# Python - Lucky Division
# https://codeforces.com/problemset/problem/122/A

number = int(input())
lucky_numbers = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
answer = 0
for x in lucky_numbers:
    if number % x == 0:
        answer = 1
        break
print("YES") if answer == 1 else print("NO")
