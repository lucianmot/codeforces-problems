# Python - Petya and Strings
# https://codeforces.com/problemset/problem/112/A 

string_1 = input().lower()
string_2 = input().lower()

if string_1 < string_2:
    print("-1")
elif string_1 > string_2:
    print("1")
else:
    print("0")
