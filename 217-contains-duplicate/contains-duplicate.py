class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()  #множество для хранения уникальных элементов
        
        for num in nums:
            #если число уже встречалось
            if num in seen:
                return True
            
            #добавляем число в множество
            seen.add(num)
        
        return False