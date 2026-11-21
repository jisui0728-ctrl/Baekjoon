import sys

input = sys.stdin.readline

i = 0 
n = int(input())
while i < n:
    score = 0
    score_2 = 0
    ox = input().rstrip()
    i += 1
    for j in ox:
        if j == "O":
            score_2 += 1
            score += score_2
        else:
            score_2 = 0
    print(score)
