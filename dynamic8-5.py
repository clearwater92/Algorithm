###
#이것이 코딩테스트다 교재의 p217 문제입니다.
###

import sys

x = int(sys.stdin.readline().rstrip())
d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1  # 점화식에 맞게 구현
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)  # 1을 뺀 것보다 2로 나눈 횟수가 더 적을지 비교
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

