n = int(input())
dp = [100000 for _ in range(n+1)]
sqr = []
for i in range(n+1):
    el = i**2
    if el > n:
        break
    sqr.append(el)
    dp[el] = 1

for i in range(n+1):
    for s in sqr:
        if i < s:
            break
        dp[i] = min(dp[i], dp[s]+dp[i-s])
print(dp[n])