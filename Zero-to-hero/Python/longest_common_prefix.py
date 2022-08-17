# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Method 1 using zip
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        for i in zip(*strs):
            if len(set(i)) == 1:
                count += 1
            else: 
                break
        return strs[0][:count]

#Method 2:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]
        compare = strs[1:]
        for i in range(len(compare)):
            count = 0
            n = len(res) if len(res) < len(compare[i]) else len(compare[i])
            for j in range(n):
                if res[j] == compare[i][j]:
                    count += 1
                else:
                    break
            res = res[:count]
        return res