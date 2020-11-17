n = int(input())

dp = [[0]*10 for _ in range(101)]

for i in range(1,10):
    dp[1][i] = 1 #한 자리수의 경우는 0,1,1,1,1,1,1,1,1,1로 초기화 시켜준다(총 9가지)

for i in range(2,n+1): # 2부터 n까지는 복잡하므로 반복
    for j in range(10):
        if j == 0:# ~자리수가 0인 경우
            dp[i][0] = dp[i-1][1]
        elif j == 9:# ~자리수가 9인 경우
            dp[i][9] = dp[i-1][8]
        else:# ~자리수가 1~8인 경우
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%1000000000)