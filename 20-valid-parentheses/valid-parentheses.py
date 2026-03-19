class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #стек для хранения открывающих скобок
        pairs = {')':'(', ']':'[', '}':'{'}

        for c in s: #проходим по каждому символу строки
            if c in '([{':
                stack.append(c) #добавляем в стек
            else:
                if not stack or stack[-1] != pairs[c]: #проверяем стек
                    return False
                stack.pop() #убираем последнюю открывающую скобку из стека

        return len(stack) == 0