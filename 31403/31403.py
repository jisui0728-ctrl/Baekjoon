import sys

input = sys.stdin.readline

a = []
for i in range(3):
    n = input().rstrip()
    a.append(n)
print(int(a[0]) + int(a[1]) - int(a[2]))
print(int(a[0] + a[1]) - int(a[2]))
