###
#이것이 코딩테스트다 교재의 p344 문제입니다.
###
from collections import deque

#n x n 크기, 바이러스가 k번까지
n, k = map(int, input().split())

graph = [] #전체 보드 정보를 담는 리스트
data = [] #바이러스에 대한 정보를 담는 리스트

#입력을 받으면서 바이러스가 있을 경우에는 어떤 바이러스인지, 시간, 좌표 정보를 data에 넣어준다
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            #초기상황에서의 바이러스기 때문에 시간은 0으로 등록
            data.append((graph[i][j],0,i,j))

#상하좌우 위치
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#정렬 이후에 큐로 옮기기
data.sort()
#빈 deque 생성 후 data를 append로 넣어주면 에러남;
queue = deque(data)



#몇초가 지났는지를 나타내는 s이고 x와y는 찾고자하는 해당 좌표이다
target_s, target_x, target_y = map(int,input().split())

#BFS 진행
while queue:
    virus, s, x, y = queue.popleft()
    #s초가 지날 경우 종료
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and 0 <= ny and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                #바이러스 정보를 큐에 넣을 때 시간을 증가 시킴
                queue.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])