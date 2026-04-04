class Solution(object):
    def floodFill(self, grid, start_row, start_col, new_color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        #исходный цвет
        orig_color = grid[start_row][start_col]
        
        #если цвет уже такой же, то ничего не делаем
        if orig_color == new_color:
            return grid
        
        n = len(grid)
        m = len(grid[0])
        
        def dfs(r, c):
            #проверка границ
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            
            #проверка цвета
            if grid[r][c] != orig_color:
                return
            
            #перекрашиваем
            grid[r][c] = new_color
            
            #рекурсивно идём к соседям
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(start_row, start_col)
        
        return grid