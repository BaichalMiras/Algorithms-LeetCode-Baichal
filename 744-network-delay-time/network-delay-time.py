class Solution(object):
    def networkDelayTime(self, times, n, k):
        import heapq
        
        #строим граф
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        #минимальные расстояния
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        
        #время, вершина
        heap = [(0, k)]
        
        while heap:
            time, node = heapq.heappop(heap)
            
            #если уже есть лучший путь - пропускаем
            if time > dist[node]:
                continue
            
            #обрабатываем соседей
            if node in graph:
                for nei, w in graph[node]:
                    new_time = time + w
                    if new_time < dist[nei]:
                        dist[nei] = new_time
                        heapq.heappush(heap, (new_time, nei))
        
        #ответ
        max_time = max(dist.values())
        
        return max_time if max_time != float('inf') else -1