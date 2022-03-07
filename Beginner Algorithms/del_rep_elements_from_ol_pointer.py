

#Double pointer method
class Solution:
    def removeDuplicates(nums):
        if len(nums) == 0:
            return 0
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                nums[l+1] = nums[r]
                l = l + 1
        return l+1
    
#test case
nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [0,1,2,3,4]

k = Solution.removeDuplicates(nums)

assert k == len(expectedNums)
for i in range (0, k):
    assert nums[i] == expectedNums[i];
    


