class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        n = len(points)
        used = [False] * n  #какие точки уже в MST
        min_dist = [float('inf')] * n  #минимальное расстояние до MST
        
        min_dist[0] = 0  #начинаем с 0-й точки
        total_cost = 0
        
        for _ in range(n):
            #находим ближайшую неиспользованную точку
            u = -1
            for i in range(n):
                if not used[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            
            #добавляем ее в MST
            used[u] = True
            total_cost += min_dist[u]
            
            #обновляем расстояния до остальных точек
            for v in range(n):
                if not used[v]:
                    x1, y1 = points[u]
                    x2, y2 = points[v]
                    
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    
                    if dist < min_dist[v]:
                        min_dist[v] = dist
        
        return total_cost