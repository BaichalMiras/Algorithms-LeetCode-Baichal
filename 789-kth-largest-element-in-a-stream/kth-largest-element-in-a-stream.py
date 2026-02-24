class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)           #превращаем в мин-кучу
        while len(self.nums) > k:          #оставляем только k наибольших
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)     #добавляем новый элемент
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)       #удаляем лишний
        return self.nums[0]                #k наибольший