#Given two integer arrays nums1 and nums2, return an array of their intersection. 
#Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#Example Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2,2]; 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Output: [4,9] Explanation: [9,4] is also accepted.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Sort nums1 and nums2 first
        nums1.sort()
        nums2.sort()
        #Using doule pointer in list nums1 and nums2, and initial value to 0
        l = 0
        r = 0
        intersection = []
        # Loop through nums1 and nums2
        while l < len(nums1) and r < len(nums2):
            # if two elements are equal, add to new  list
            if nums1[l] == nums2[r]:
                intersection.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
        return intersection