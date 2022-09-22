# Python - Pashmak and Garden
# https://codeforces.com/problemset/problem/459/A
# Incomplete, still working on it, got to test 6 or 7

from itertools import product
initList = list(map(int, input().split(" ")))
# initList = [0, 0, 0, 1]

uniqueList = list(set(initList))
if len(uniqueList) > 2:
    print("-1")
else:
    corner1 = tuple(initList[:len(initList) // 2])
    corner2 = tuple(initList[len(initList) // 2:])
    combiList = list(product(uniqueList, repeat=2))
    combiList.remove(corner1)
    combiList.remove(corner2)
    answer = combiList[0] + combiList[1]
    answer = list(answer)
    answer = list(map(str, answer))
    print(' '.join(answer))
