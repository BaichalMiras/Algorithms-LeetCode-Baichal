class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        #минимум монет для каждой суммы
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    #пробуем взять монету
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]