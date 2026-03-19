class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []  #cтек для хранения чисел

        for t in tokens:  #проходим по всем токенам
            if t in ["+", "-", "*", "/"]: 
                b = stack.pop()  #второй операнд
                a = stack.pop()  #первый операнд

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    #деление с округлением к нулю
                    if a * b < 0:  #если результат отрицательный
                        stack.append(- (abs(a) // abs(b)))
                    else:
                        stack.append(a // b)

            else:
                stack.append(int(t))  #добавляем число

        return stack[0]  #итоговый результат