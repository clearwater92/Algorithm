n = int(input())

arr = []
arr.append(0)
for i in range(1,n+1):
    arr.append(int(input()))
dp = [0]
dp.append(arr[1])
if n > 1:
    dp.append(dp[1]+arr[2])

#dp[3] = max(dp[2], dp[1]+arr[3], arr[2]+arr[3])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]))

print(dp[n])