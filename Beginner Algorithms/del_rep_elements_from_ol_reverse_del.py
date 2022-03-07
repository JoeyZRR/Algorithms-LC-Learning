# Remove repeat elements from ordered list
# Return length of none repeat list
# Example: Input: [0,0,1,1,1,2,2,3,3,4], output:[0,1,2,3,4], Length:5

# Reverse delete method
class Solution:
    def removeDuplicates(nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)
    
#test case from LC
nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [0,1,2,3,4]

k = Solution.removeDuplicates(nums)

assert k == len(expectedNums)
for i in range (0, k):
    assert nums[i] == expectedNums[i];