###
#이것이 코딩테스트다 교재의 p197 문제입니다.
###

import sys
n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(list, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return binary_search(list, target, start, mid-1)
    else:
        return binary_search(list, target, mid+1, end)
nlist.sort()

for i in mlist:
    result = binary_search(nlist, i, 0, len(nlist))
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')