# Python - Word
# https://codeforces.com/problemset/problem/59/A

word = input()
param = 0

for x in word:
    if x.isupper() == True:
        param+=1
    else:
        param-=1

if param <= 0:
    print(word.lower())
else:
    print(word.upper())
