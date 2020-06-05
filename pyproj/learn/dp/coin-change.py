def coinchange(coin,n):
    m=len(coin)
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(0,m):
        dp[i][0]=1
    for i in range(1,m):
        for j in range(1,n+1):
            if coin[i]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-coin[i]]
coin=[1,2,3]
n=4
print(coinchange(coin,n))
        