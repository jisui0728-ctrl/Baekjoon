import sys

input = sys.stdin.readline

r = []
count = 0 

for i in range(0,10):
    n = int(input())
    r.append(n % 42)

print(len(set(r)))