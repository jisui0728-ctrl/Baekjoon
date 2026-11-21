import sys

input = sys.stdin.readline

n = int(input())
number = [0] * 10001

for _ in range(n):
    number[int(input())] += 1

for i in range(1, 10001):
    if number[i] > 0:
        for _ in range(number[i]):
            print(i)
