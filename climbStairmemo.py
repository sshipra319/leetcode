def climbStairs(n):
    memo = [0] * (n + 2)
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]