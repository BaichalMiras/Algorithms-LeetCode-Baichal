class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #если длины разные - сразу false
        if len(s) != len(t):
            return False
        
        count = {}  #словарь
        
        #считаем символы строки s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        #уменьшаем по строке t
        for ch in t:
            if ch not in count:
                return False
            
            count[ch] -= 1
            
            #если стало меньше 0 - лишний символ
            if count[ch] < 0:
                return False
        
        return True