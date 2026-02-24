class Solution(object):

    def findKthLargest(self, nums, k):
        n = len(nums)

        #BUILD-MAX-HEAP
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        #k-1 раз извлекаем максимум
        for i in range(n - 1, n - k, -1):
            nums[0], nums[i] = nums[i], nums[0]  #перенос максимума в конец
            self.heapify(nums, i, 0)             #восстановление max-heap

        return nums[0]  #k наибольший

    def heapify(self, arr, heap_size, i):
        largest = i
        left = 2 * i + 1      #левый потомок
        right = 2 * i + 2     #правый потомок

        #ищем наибольший среди родителя и потомков
        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        #если родитель не самый большой, то меняем и продолжаем
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, heap_size, largest)