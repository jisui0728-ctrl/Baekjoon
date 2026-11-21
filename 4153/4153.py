import sys

input = sys.stdin.readline
distance_set = []

while True:
    distance = list(map(int,input().split()))
    
    if distance[0] == 0 and distance[1] == 0 and distance[2] == 0:
        break
    distance_set.append(distance)

for i in range(0,len(distance_set)):
    if ((distance_set[i][2])**2 == (distance_set[i][0])**2 + (distance_set[i][1])**2) or ((distance_set[i][1])**2 == (distance_set[i][0])**2 + (distance_set[i][2])**2) or ((distance_set[i][0])**2 == (distance_set[i][1])**2 + (distance_set[i][2])**2):
        print("right")
    else:
        print("wrong")
    