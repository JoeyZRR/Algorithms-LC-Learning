# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example:

# Given the 2D grid:

# INF -1 0 INF
# INF INF INF -1
# INF -1 INF -1
# 0 -1 INF INF
# After running your function, the 2D grid should be:

# 3 -1 0 1
# 2 2 1 -1
# 1 -1 2 -1
# 0 -1 3 4
# ————————————————

from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        col = len(rooms[0])
        visited = set()
        q = deque()
        
        def nextRoom(r, c):
            # If adjust room over edge or visited or wall, ignore
            if (r < 0 or r == rows or c < 0 or c == col or rooms[r][c] == -1 or (r, c) in visited):
                return
            visited.add((r,c))
            q.append([r, c])
        
        #BFS from all door positions          
        for r in range(rows):
            for c in range(col):
                # Record door position:
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        # Initial BFS distince        
        distince = 0
        while q:
            for i in range(len(q)):
                # (r, c) from que
                r, c = q.popleft()
                
                rooms[r][c] = distince
                #Add all adjust room to q
                nextRoom(r + 1, c)
                nextRoom(r - 1, c)
                nextRoom(r, c + 1)
                nextRoom(r, c - 1)
            distince += 1