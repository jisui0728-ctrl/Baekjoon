import sys

input = sys.stdin.readline

n = int(input())
t = list(map(int,input().split()))
count = 0

for i in range(0,n):
    result = []
    for j in range(0,t[i]):
        if t[i] % (j+1) == 0:
            result.append(j+1)
    if len(result) == 2:
        count += 1
print(count)