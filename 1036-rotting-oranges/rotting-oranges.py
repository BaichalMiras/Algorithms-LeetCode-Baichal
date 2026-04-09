class Solution(object):
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        queue = []  #список вместо очереди
        fresh = 0
        
        #cобираем все гнилые и считаем свежие
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        index = 0  #указатель на начало очереди
        
        while index < len(queue) and fresh > 0:
            size = len(queue) - index  #cколько элементов в этом "слое"
            
            for _ in range(size):
                x, y = queue[index]
                index += 1
                
                # вверх
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    queue.append((x-1, y))
                    fresh -= 1
                
                #вниз
                if x < rows-1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    queue.append((x+1, y))
                    fresh -= 1
                
                #влево
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    queue.append((x, y-1))
                    fresh -= 1
                
                #вправо
                if y < cols-1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    queue.append((x, y+1))
                    fresh -= 1
            
            minutes += 1
        
        if fresh > 0:
            return -1
        
        return minutes