class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)/2
        if len(nums) % 2 == 0:
            res = (nums[int(n)]+nums[int(n)-1])/2
        else:
            res = nums[len(nums)//2]
        return res