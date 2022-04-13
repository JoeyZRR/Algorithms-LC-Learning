#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

#Example: Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Function for check duplicate
        def isvaild(filteredList):
            #Filter all "." in the list
            nums = list(filter(lambda x:x != '.', filteredList))
            return len(set(nums)) == len(nums)
        
        #Check duplicate for all rows
        for row in board:
            if not isvaild(row):
                return False
        
        #Check duplicate for all columns
        for column in zip(*board):
            if not isvaild(column):
                return False
        
        #Check duplicate in each 3 x 3 sub-boxes of the grid
        for row in range(3):
            for column in range(3):
                temp = [board[i][j] for i in range(row*3, row*3+3) for j in range(column*3, column*3+3)]
                if not isvaild(temp):
                    return False
        return True