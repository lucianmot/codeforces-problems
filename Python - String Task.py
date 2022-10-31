# Python - String Task
# https://codeforces.com/problemset/problem/118/A

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z", "w"]
answer = ""
word = input().lower()
for x in word:
    if x in consonants:
        answer+="."
        answer+=str(x)
print(answer)
