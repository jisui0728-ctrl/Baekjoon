import sys

input = sys.stdin.readline

number = []

while True:
    n = input().rstrip()
    if int(n) == 0:
        break
    number.append(n)

for i in range(0,len(number)):
    if number[i][:] == number[i][::-1] and number[i][0] != '0':
        print("yes")
    else:
        print("no")