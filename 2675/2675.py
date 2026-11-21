import sys

input = sys.stdin.readline

n = int(input())
s_set = []

for i in range(n):
    a = list(map(str,input().split()))
    s_set.append(a)

for j in range(n):
    s_result = ''
    s = list(s_set[j][1])
    for k in s:
        s_result += (k * (int(s_set[j][0])))
    print(s_result)