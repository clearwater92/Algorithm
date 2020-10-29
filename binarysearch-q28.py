###
#이것이 코딩테스트다 교재의 p368 문제입니다.
###

import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
target = 0
for x in range(0, len(arr)):
    if x == arr[x]:
        target = x
result = binary_search(arr, target, 0, len(arr))
print(result)