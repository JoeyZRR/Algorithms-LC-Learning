# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:  Input: s = "leetcode"
# Output: 0

# Example 2:  Input: s = "loveleetcode"
# Output: 2

# Example 3:  Input: s = "aabb"
# Output: -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in s:
            #.find() returns first position of that character, .rfind() returns last position of that character. 
            # So if s.find(i) == s.rfind(i) means the i it's unique.
            if s.find(i) == s.rfind(i):
                return s.find(i)
        return -1