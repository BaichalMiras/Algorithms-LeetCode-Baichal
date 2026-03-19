class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [0] * k  #массив фиксированного размера для хранения элементов
        self.max_size = k  #максимальный размер очереди
        self.front = 0  #начало очереди
        self.rear = -1  #конец очереди
        self.count = 0  #текущее кол-во элементов

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():  #проверяем, заполнена ли очередь
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value  #вставляем элемент в конец
        self.count += 1  #увеличиваем кол-во элементов
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():  #проверяем, пуста ли очередь
            return False
        self.front = (self.front + 1) % self.max_size  #двигаем начало по кругу
        self.count -= 1  #уменьшаем количество элементов
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():  #если очередь пустая
            return -1
        return self.queue[self.front]  #возвращаем первый элемент

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():  #если очередь пустая
            return -1
        return self.queue[self.rear]  #возвращаем последний элемент

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0  #очередь пуста, если нет элементов

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.max_size  #очередь полная, если достигнут максимум
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()