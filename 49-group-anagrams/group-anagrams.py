class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}  #словарь
        
        for s in strs:
            #сортируем слово и используем как ключ
            sorted_key = ''.join(sorted(s))
            
            if sorted_key not in anagram_map:
                anagram_map[sorted_key] = []
            
            anagram_map[sorted_key].append(s)
        
        return anagram_map.values()