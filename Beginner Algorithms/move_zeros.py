#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
#Example: Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Loop through the list, if there is a zero, add a zero to the end of the list, then delete that zero
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.insert(len(nums), 0)
                del nums[i]