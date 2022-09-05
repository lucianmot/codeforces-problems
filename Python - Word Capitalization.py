# Python - Word Capitalization
# https://codeforces.com/contest/281/problem/A

word = input()
wordList = list(word)

if wordList[0].isupper():
    print(word)
else:
    wordList[0] = wordList[0].capitalize()
    print(''.join(wordList))
