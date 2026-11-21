import sys

input = sys.stdin.readline

plus = []

while True:
    a,b = map(int,input().split())
    if a == 0 and b ==0:
        break
    plus.append(a+b)

for i in range(0,len(plus)):
    print(plus[i])
        