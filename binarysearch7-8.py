import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
ricecake = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(ricecake)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in ricecake:
        if x > mid:
            total += x - mid
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)