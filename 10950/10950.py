import sys

input = sys.stdin.readline

n = int(input())
plus = []

for i in range(0,n):
    a = list(map(int,input().split()))
    plus.append(a[0]+a[1])

for j in range(0,n):
    print(plus[j])
