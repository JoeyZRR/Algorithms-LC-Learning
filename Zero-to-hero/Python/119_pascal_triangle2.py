# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex+1)
        if rowIndex < 2:
            return res
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                res[j] = res[j-1]+res[j]
        return res