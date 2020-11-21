n = int(input())
arr = list(map(int,input().split()))
dpp = [0 for i in range(n)]
dpm = [0 for i in range(n)]
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dpp[i] < dpp[j]:
            dpp[i] = dpp[j]
    dpp[i] += 1
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j] and dpm[i] <dpm[j]:
            dpm[i] = dpm[j]
    dpm[i] += 1
for i in range(n):
    dp[i] = dpp[i] + dpm[i] - 1

print(max(dp))