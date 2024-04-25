def min_coins(coins, amount):
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != INF else -1


inp = open("input4.txt", "r")
out = open("output4.txt", "w")
N, amount = [int(i) for i in inp.readline().split()]
coins = [int(i) for i in inp.readline().split()]
result = min_coins(coins, amount)
out.write(str(result))

