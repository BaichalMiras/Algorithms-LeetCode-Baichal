class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #базовые случаи
        if n <= 2:
            return n
        
        prev2 = 1
        prev1 = 2
        
        #строим решение снизу вверх (табуляция)
        for i in range(3, n + 1):
            curr = prev1 + prev2  #основной переход
            
            #сдвигаем значения
            prev2 = prev1
            prev1 = curr
        
        return prev1