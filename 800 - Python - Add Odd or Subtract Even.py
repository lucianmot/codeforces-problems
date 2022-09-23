# Python - Add Odd or Subtract Even
# Rating - 800
# https://codeforces.com/contest/1311/problem/A

testCases = int(input())

for i in range(testCases):
    a, b = map(int, input().split(" "))

    aType = "Even" if a % 2 == 0 else "Odd"
    bType = "Even" if b % 2 == 0  else "Odd"

    if a == b:
        print("0")
    elif a < b:
        if aType == "Odd" and bType == "Odd":
            print("2")
        elif aType == "Even" and bType == "Even":
            print("2")
        else:
            print("1")
    elif a > b:
        if aType == "Odd" and bType == "Odd":
            print("1")
        elif aType == "Even" and bType == "Even":
            print("1")
        else:
            print("2")
