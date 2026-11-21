import sys

input = sys.stdin.readline

test_case = int(input())
number = []

for i in range(0,test_case):
    n = int(input())
    number.append(n)

number.sort()

for j in range(0,test_case):
    print(number[j])