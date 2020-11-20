n = int(input())
dt = list(map(int,input().split()))
dp = [0 for i in range(n)]
dp[0] = dt[0]
for i in range(1, n):
    dp[i] = max(dt[i]+dp[i-1], dt[i])

print(max(dp))