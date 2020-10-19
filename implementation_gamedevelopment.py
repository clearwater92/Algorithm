###
#이것이 코딩테스트다 교재의 p118번 문제입니다.
###

n, m = map(int, input().split())
# 방문한 위치
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

# 전체 맵 정보를 입력 받기
arr = []
for i in range(0, n):
    arr.append(list(map(int, input().split())))

result = 0

#북,동,남,서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = 0

#왼쪽으로 90도씩 회전하는 함수
def turn_left():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -= 1

turn_time = 0
result = 1
while True:
    #왼쪽으로 90도 회전하고 다음 좌표를 설정
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #다음 좌표가 가보지 않았고 육지인 경우
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        x = nx
        y = ny
        d[nx][ny] = 1
        result += 1
        turn_time = 0
        continue
    #다음 좌표가 가보았거나 바다인 경우
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        #다음 좌표를 뒤로 한 칸 전진한 곳으로
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤가 바다로 막혀있는 경우
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(result)
