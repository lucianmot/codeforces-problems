# Python - Beautiful Matrix
# https://codeforces.com/problemset/problem/263/A

points = [[4, 3, 2, 3, 4], [3, 2, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 2, 3], [4, 3, 2, 3, 4]]
example = [list(map(int, input().split(" "))), list(map(int, input().split(" "))), list(map(int, input().split(" "))), list(map(int, input().split(" "))), list(map(int, input().split(" ")))]
count_1 = 0
index_1 = 0
for x in example:
    if 1 in x:
        index_1 = x.index(1)
        break
    count_1+=1
print(points[count_1][index_1])
