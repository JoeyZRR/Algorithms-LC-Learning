class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Conside the case that k > length of list
        k %= len(nums)
        # Using python slice to rotate
        nums[:] = nums[-k:] + nums[:-k]
        