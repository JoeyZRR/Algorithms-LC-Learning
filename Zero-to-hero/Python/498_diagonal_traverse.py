# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
# Nums of row
        row = len(mat)
# Nums of column
        col = len(mat[0])
# Nums of diagonal
        diagonal = row + col - 1
# Coordinate of current (row, col)
        r, c = 0, 0
        res = []
        for i in range(diagonal):
# If even means go up
            if i % 2 == 0:
                while r >= 0 and c < col:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
                if c < col:
                    r += 1
                else:
                    r += 2
                    c -= 1
            else:
                while r < row and c >= 0:
                    res.append(mat[r][c])
                    c -= 1
                    r += 1
                if r < row:
                    c += 1
                else:
                    c += 2
                    r -= 1
        return res