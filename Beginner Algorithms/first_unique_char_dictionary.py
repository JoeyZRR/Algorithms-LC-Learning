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
        #Use collection.Counter to assign every char in s and the number they appeared into dct
        dct = collections.Counter(s)
        for i, n in enumerate(s):
            if dct[n] == 1:
                return i
        return -1