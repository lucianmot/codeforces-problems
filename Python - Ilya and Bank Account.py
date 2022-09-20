# Python - Ilya and Bank Account
# https://codeforces.com/problemset/problem/313/A

bankAcc = int(input())

if bankAcc < 0:
    bankList = list(str(bankAcc))
    if int(bankList[-2]) > int(bankList[-1]):
        del bankList[-2]
    else:
        del bankList[-1]
    bankAnswer = ''.join(bankList)
    print(int(bankAnswer))
else:
    print(bankAcc)
