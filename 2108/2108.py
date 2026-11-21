import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = []

for i in range(0,n):
    numbers.append(int(input()))

numbers.sort()

counter = Counter(numbers)
max_freq = max(counter.values())

modes = [num for num, freq in counter.items() if freq == max_freq] #구글링함zz
modes.sort()

print(round(sum(numbers) / len(numbers)))
print(numbers[round(len(numbers) // 2)])
print(modes[0] if len(modes) == 1 else modes[1])
print(max(numbers) - min(numbers))