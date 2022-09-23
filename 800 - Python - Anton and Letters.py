# Python - Anton and Letters
# https://codeforces.com/problemset/problem/443/A

letters = input()
if letters == "{}":
    print("0")
else:   
    letters = letters[1:-1]
    letters = list(set(letters.split(", ")))
    print(len(letters))
