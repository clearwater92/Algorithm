n = int(input())
dt = [0 for _ in range(301)]
for i in range(n):
    dt[i] = int(input())

dp = [0 for _ in range(301)]

dp[0] = dt[0]
dp[1] = dt[0] + dt[1]
dp[2] = max(dt[0]+dt[2], dt[1]+dt[2])

for i in range(3, n):
    dp[i] = max(dp[i-3]+dt[i-1]+dt[i], dp[i-2]+dt[i])

print(dp[n-1])