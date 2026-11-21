import sys

input = sys.stdin.readline

plus = []

while True:
    try:
        a,b = map(int,input().split())
        plus.append(a+b)
    except:
        break

for i in range(0,len(plus)):
    print(plus[i])
