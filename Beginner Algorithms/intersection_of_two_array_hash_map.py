#Given two integer arrays nums1 and nums2, return an array of their intersection. 
#Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#Example Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2,2]; 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Output: [4,9] Explanation: [9,4] is also accepted.
import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Assign both nums1 and nums2 to hashmap
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        #Using & operator to get elements in both nums1 and nums2
        num = num1 & num2
        return list(num.elements())
        