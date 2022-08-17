# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from collections import deque


class Solution:
    def numIslands(self, grid: [[]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append([r, c])
            
            while q:
                r, c = q.popleft()
                if 0 <= r < rows and 0 <= c < cols  and (r, c ) not in visited and grid[r][c] == '1':
                    visited.add((r,c))
                    q.append([r+1, c])
                    q.append([r-1, c])
                    q.append([r, c+1])
                    q.append([r, c-1])

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
    
print(Solution().numIslands(grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))