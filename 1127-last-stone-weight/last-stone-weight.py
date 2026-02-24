class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        hp = [None] + stones
        size = len(stones)

        def max_heapify(A, i, n):
            l, r = 2 * i, 2 * i + 1 
            largest = i
            if l <= n and A[l] > A[i]: 
                largest = l
            if r <= n and A[r] > A[largest]: 
                largest = r
            if largest != i:
                A[i], A[largest] = A[largest], A[i] 
                max_heapify(A, largest, n) 

        def extract_max(A, n):
            if n < 1: return 0, 0
            res = A[1] #корень всегда максимум
            A[1] = A[n] #замена последним элементом
            n -= 1
            max_heapify(A, 1, n) #восстановление кучи 
            return res, n

        #BUILD-MAX-HEAP
        for i in range(size // 2, 0, -1): 
            max_heapify(hp, i, size)

        #основной процесс
        while size > 1:
            #извлекаем два самых тяжелых камня
            y, size = extract_max(hp, size)
            x, size = extract_max(hp, size)
            
            if x != y:
                #вставляем разницу обратно в кучу
                new_stone = y - x
                size += 1
                hp[size] = new_stone
                #bubble-up
                i = size
                while i > 1 and hp[i // 2] < hp[i]:
                    hp[i // 2], hp[i] = hp[i], hp[i // 2]
                    i //= 2

        return hp[1] if size == 1 else 0