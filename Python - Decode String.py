# Python - Decode String
# https://codeforces.com/contest/1729/problem/B

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
testCases = int(input())

for i in range(testCases):
  whatever = input()
  workArr = list(input())
  index = len(workArr) - 1
  counter = 0
  answer = []
  while index >= 0:
    if workArr[index] == "0":
      number = workArr[index - 2] + workArr[index - 1]
      answer.append(int(number))
      index-=3
    else:
      answer.append(int(workArr[index]))
      index-=1
  answer = reversed(answer)
  real_answer = []
  for x in answer:
    real_answer.append(alphabet[x-1])
  print(''.join(real_answer))
