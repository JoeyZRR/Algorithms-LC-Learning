# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1,numRows+1)]
        for m in range(2, numRows):
            for n in range(1, m):
                res[m][n] = res[m-1][n-1] + res[m-1][n]
        return res
