class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        #максимум до прошлого и через один
        a = nums[0]
        b = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            #берем лучшее
            c = max(b, a + nums[i])
            
            a = b
            b = c
        
        return b