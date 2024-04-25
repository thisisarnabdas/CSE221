def count_ways(N):
    dp = [0] * (N + 1)
    dp[0] = dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]


inp = open("input3.txt", "r")
out = open("output3.txt", "w")
N = int(inp.readline())
result = count_ways(N)
out.write(str(result))
