class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        s = sum(nums)
        
        #если нечетная - нельзя
        if s % 2 != 0:
            return False
        
        t = s // 2
        
        #можно ли собрать сумму
        dp = [False] * (t + 1)
        dp[0] = True
        
        for x in nums:
            #идем с конца
            for i in range(t, x - 1, -1):
                if dp[i - x]:
                    dp[i] = True
        
        return dp[t]