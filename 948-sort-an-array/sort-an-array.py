class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #базовый случай рекурсии
        if len(nums) <= 1:
            return nums
        
        #делим массив пополам
        mid = len(nums) // 2
        left_part = nums[:mid]
        right_part = nums[mid:]
        
        #рекурсивно сортируем части
        left_sorted = self.sortArray(left_part)
        right_sorted = self.sortArray(right_part)
        
        #возвращаем отсортированные части
        return self.merge(left_sorted, right_sorted)
    
    
    def merge(self, left, right):
        result = []
        i = 0
        j = 0
        
        #cливаем два отсортированных массива
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        #добавляем оставшиеся элементы
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

        