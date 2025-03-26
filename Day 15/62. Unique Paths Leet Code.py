class Solution(object):
    def uniquePaths(self, m, n):
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]