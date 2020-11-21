tc = int(input())

dp = [0 for i in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

n = []
for i in range(tc):
    n.append(int(input()))

for j in n:
    print(dp[j])
