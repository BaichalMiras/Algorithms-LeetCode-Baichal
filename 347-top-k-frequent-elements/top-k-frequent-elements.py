class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #сбор данных: объект (число) и ключ (частота)
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        #представление кучи в виде массива (индексация с 1)
        #элемент = [частота, число]
        hp = [None] + [[f, v] for v, f in counts.items()]
        n = len(hp) - 1

        def max_heapify(A, i, size):
            l, r = 2 * i, 2 * i + 1
            largest = i
            if l <= size and A[l][0] > A[i][0]:
                largest = l
            if r <= size and A[r][0] > A[largest][0]:
                largest = r
            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                max_heapify(A, largest, size)

        #BUILD-MAX-HEAP: проход снизу вверх
        for i in range(n // 2, 0, -1):
            max_heapify(hp, i, n)

        #извлечение k максимумов
        res = []
        curr_size = n
        for _ in range(k):
            res.append(hp[1][1]) #корень - максимум
            hp[1] = hp[curr_size]
            curr_size -= 1
            max_heapify(hp, 1, curr_size)
            
        return res