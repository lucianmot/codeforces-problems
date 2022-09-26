# Python - Chewbaсca and Number
# Rating - 1200
# https://codeforces.com/problemset/problem/514/A

number = input()
arr = [int(x) for x in str(number)]
answer = ""

counter = 0

for x in arr:
    if x == 9 and counter == 0:
        answer+=str(x)
    elif 9 - x < x:
        answer+=str(9-x)
    else:
        answer+=str(x)
    counter+=1

print(answer)
