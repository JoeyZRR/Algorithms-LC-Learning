# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
#Input: nums = [1,2,3,1] Output: true; Input: nums = [1,1,1,3,3,4,3,2,4,2] Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Using the set to remove duplicate from list, 
        # if length of set = length of list, that means no duplicate 
        # then we can return false means there are no duplicate in the list.
        if len(nums) == len(set(nums)):
            return False
        else:
            return True