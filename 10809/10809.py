import sys

input = sys.stdin.readline

s = input().rstrip()
alpha_List = list(map(chr, range(97, 123))) 

for i in alpha_List:
    if i in s:
        print(s.find(i),end=" ")
    else:
        print(-1,end=" ")
