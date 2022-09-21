# Python - Cheap Travel
# https://codeforces.com/problemset/problem/466/A

n, m, a, b = list(map(int, input().split(" ")))

sum = 0
specialTicketAvg = b / m

if specialTicketAvg < a:
    sum+=int(n / m) * b
    n = n % m
    if n * a < b: 
        sum+=n*a
    else:
        sum+=b
else:
  sum = n * a

print(int(sum))
