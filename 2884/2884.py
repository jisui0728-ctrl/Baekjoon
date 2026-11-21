import sys

input = sys.stdin.readline

h,m = map(int,input().split())

if m - 45 < 0 and h == 0 :
    print(23,(60+m) - 45 )
elif m - 45 < 0 and h != 0:
    print(h-1,(60+m) - 45) 
else:
    print(h,m-45)