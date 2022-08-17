# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# Example: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Rotate Up and dowm
        for i in range(len(matrix)//2):
            matrix[i], matrix[len(matrix)-i-1] = matrix[len(matrix)-i-1], matrix[i]
            
        # Rotate the symmetry
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return matrix
print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))