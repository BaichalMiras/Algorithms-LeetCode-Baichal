class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        def dfs(r, c):
            #проверка границ
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            
            #если это вода, то выходим
            if grid[r][c] == "0":
                return
            
            #помечаем клетку как посещённую (затапливаем)
            grid[r][c] = "0"
            
            #обходим соседей
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        islands = 0
        
        #проходим по всей сетке
        for i in range(n):
            for j in range(m):
                #если нашли землю, то это новый остров
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)  #обходим весь остров
        
        return islands