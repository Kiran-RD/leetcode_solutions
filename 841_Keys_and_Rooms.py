# DFS

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        
        def dfs(room):
            if visited[room]:
                return
            
            visited[room] = True
            
            for i in rooms[room]:
                dfs(i)
        
        dfs(0)

        if False in set(visited):
            return False
        return True
      
# BFS

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        q = deque([0])
        while len(q):
            room = q.popleft()
            visited[room] = True
            for i in rooms[room]:
                if not visited[i]:
                    q.append(i)
            
        if False in set(visited):
            return False
        return True
