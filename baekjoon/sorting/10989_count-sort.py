#계수정렬(메모리 8메가 제한, 리스트 하나로)
import sys
n = int(sys.stdin.readline().rstrip())

#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * 10001

for i in range(n):
    input_v = int(sys.stdin.readline())
    count[input_v] += 1

for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i)