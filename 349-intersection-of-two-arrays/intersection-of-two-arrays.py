class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)  #элементы первого массива
        result = set()    #множество для результата
        
        for num in nums2:
            #если элемент есть в первом массиве
            if num in set1:
                result.add(num)
        
        return list(result)