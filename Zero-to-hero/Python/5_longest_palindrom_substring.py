s = "babad"

# Medthod 1:
# def longestPalindrome(s: str) -> str:
#         if not s:
#             return ''
#         def expandAroundCenter(s, left, right):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return right - left - 1
        
#         start, end = 0, 0
#         for i in range(len(s)):
#             len1 = expandAroundCenter(s, i, i)
#             len2 = expandAroundCenter(s, i, i+1)
#             length = max(len1, len2)
#             if length > end-start:
#                 start = i - (length-1)//2
#                 end = i + length//2
#         return s[start:end+1]

# Method 2:
class Solution:
    def longestPalindrome(self, s: str) -> str:
            if len(s) < 2 or s == s[::-1]:
                return s
            res = s[0]
            maxlen = 1
            for i in range(1, len(s)):
                odd = s[i - maxlen - 1: i + 1]
                even = s[i - maxlen: i + 1]
                if odd == odd[::-1] and i - maxlen - 1 >= 0:
                    res = odd
                    maxlen += 2
                    continue
                if even == even[::-1] and i - maxlen >= 0:
                    res = even
                    maxlen += 1
                    continue
            return res    
print(Solution().longestPalindrome(s))