class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #подготавливаем три указателя с конца
        i = m - 1  #последний элемент части nums1
        j = n - 1  #последний элемент nums2
        k = m + n - 1  #конец массива nums1 (туда будем вставлять элементы)
        
        #пока есть элементы в nums2
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1