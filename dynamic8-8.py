###
#이것이 코딩테스트다 교재의 p226 문제입니다.
###

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

#m의 최대 크기가 10000이므로 불가능을 의미하는 수인 10001로 초기화
d = [10001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j], d[j-arr[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])