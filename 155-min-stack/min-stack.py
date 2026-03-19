class MinStack(object):

    def __init__(self):
        self.stack = [] #основной стек для хранения всех элементов
        self.min_stack = [] #стек для хранения текущих минимумов

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val) #добавляем элемент в основной стек
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val) #добавляем в стек минимумов

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.min_stack[-1]: #если удаляемый элемент равен текущему минимуму
            self.min_stack.pop() #удаляем его из стека минимумов
        self.stack.pop() #удаляем элемент из основного стека

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] #возвращаем верхний элемент стека

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] #возвращаем текущий минимум

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()