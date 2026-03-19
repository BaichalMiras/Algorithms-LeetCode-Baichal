class MyQueue(object):

    def __init__(self):
        self.stack_in = []  #стек для добавления элементов
        self.stack_out = []  #стек для извлечения элементов

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)  #добавляем элемент в входной стек

    def pop(self):
        """
        :rtype: int
        """
        self.peek()  #правильный порядок элементов
        return self.stack_out.pop()  #удаляем и возвращаем первый элемент очереди

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack_out: 
            while self.stack_in:  #переносим все элементы из входного стека
                self.stack_out.append(self.stack_in.pop())  #переворачиваем порядок
        return self.stack_out[-1]  #возвращаем первый элемент очереди

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out  #очередь пуста, если оба стека пусты