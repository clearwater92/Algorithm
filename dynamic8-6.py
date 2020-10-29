###
#이것이 코딩테스트다 교재의 p220 문제입니다.
###
import sys

n = int(sys.stdin.readline().rstrip())
#array는 식량창고 리스트
array = list(map(int, sys.stdin.readline().rstrip().split()))

#DP테이블 초기화
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])

