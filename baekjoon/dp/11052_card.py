n = int(input())
dt = list(map(int,input().split()))
dt.insert(0,0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i-j]+dt[j], dp[i])

print(dp[n])