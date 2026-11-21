import sys

input = sys.stdin.readline

n = int(input())
a = input().rstrip()
sum = 0

for i in range(0,n):
    sum += int(a[i])
print(sum)