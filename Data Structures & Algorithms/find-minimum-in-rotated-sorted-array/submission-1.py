class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        for i in range(len(nums)):
            m = min(nums[i], m)
        
        return m
        