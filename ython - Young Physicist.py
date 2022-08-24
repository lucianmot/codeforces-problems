# Python - Young Physicist
# https://codeforces.com/problemset/problem/69/A

loop_times = int(input())
vector_x = 0
vector_y = 0
vector_z = 0
for x in range(loop_times):
    vector=list(map(int, input().split(" ")))
    vector_x+=vector[0]
    vector_y+=vector[1]
    vector_z+=vector[2]
print("YES") if vector_x==vector_y==vector_z==0 else print("NO")
