import sys

input = sys.stdin.readline

test_data = int(input())
room_data = []

for i in range(0,test_data):
    data = list(map(int,input().split()))
    room_data.append(data)

for j in range(0,test_data):
    room = []
    for k in range(1,room_data[j][1]+1):
        f = 1
        while f < room_data[j][0]+1 :
            if k < 10:
                room.append("{}".format(str(f) + "0" + str(k)))
            else:
                room.append("{}".format(str(f) + str(k))) 
            f += 1
    print(room[room_data[j][2] - 1])             
