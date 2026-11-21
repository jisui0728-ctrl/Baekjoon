import sys,math

input = sys.stdin.readline

n = int(input())
number_string = str(math.factorial(n))
end_index = 0

for i in range(0,len(number_string)):
    if number_string[len(number_string) - (i+1)] != number_string[len(number_string) - (i+2)]:
        end_index += len(number_string) - (i+2)
        break

print((number_string[(end_index + 1) : (len(number_string))]).count('0'))