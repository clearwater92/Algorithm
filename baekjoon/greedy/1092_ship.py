from collections import deque

n = int(input())
crane = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))

time = 0 #시간
checked = [0 for _ in range(m)] #박스를 옮겼는 지 여부
count = 0 #옮긴 박스의 개수

crane.sort(reverse=True)
boxes.sort(reverse=True)

positions = [0]*n #크레인의 위치(총 박스의 개수보다 클 수 없다)

#가장 큰 박스가 가장 큰 크레인보다 무거울 경우 -1를 리턴
if max(boxes) > max(crane):
    print(-1)
else:
    while count < len(boxes): #옮긴 박스가 총 박스 수 보다 적으면 반복
         for i in range(n):
             print(positions, checked)
             while positions[i] < len(boxes):
                 if not checked[positions[i]] and crane[i] >= boxes[positions[i]]:#아직 안옮긴 박스 중에서, 옮길 수 있는 박스를 만날때까지 반복
                     checked[positions[i]] = True
                     positions[i] += 1
                     count += 1
                     break
                 positions[i] += 1
         time += 1
    print(time)