def Knapsack(W, profit, weight, n):
    dp = []
    for i in range(n + 1):
        row = []
        for j in range(W + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weight[i - 1] <= j:
                # If the current item's weight is less than or equal to the current capacity,
                # consider the maximum of two cases:
                # 1. Including the current item (value + value of the remaining capacity)
                # 2. Excluding the current item (value of the remaining capacity without the current item)
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + profit[i - 1])
            else:
                # If the current item's weight is more than the current capacity, exclude the item
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


# Example usage
W = 7
profit = [1, 4, 5, 7]
weight = [1, 3, 4, 5]
n = len(profit)

max_profit = Knapsack(W, profit, weight, n)
print("Maximum Profit =", max_profit)