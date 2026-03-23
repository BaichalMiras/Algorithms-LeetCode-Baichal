class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}  #словарь
        
        for i in range(len(nums)):
            complement = target - nums[i]  #какое число нужно
            
            #если такое число уже было
            if complement in hash_map:
                return [hash_map[complement], i]
            
            #сохраняем текущее число
            hash_map[nums[i]] = i