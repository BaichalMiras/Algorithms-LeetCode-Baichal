class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        left = 0
        right = len(letters) - 1
        
        #бинарный поиск
        while left <= right:
            mid = (left + right) // 2
            
            #если текущая буква больше target,
            #пробуем найти ещё меньшую подходящую слева
            if letters[mid] > target:
                right = mid - 1
            else:
                #ищем справа
                left = mid + 1
        
        #если подходящей буквы нет,
        #делаем переход к первой
        return letters[left % len(letters)]
