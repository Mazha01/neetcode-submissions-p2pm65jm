class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        for i in range(len(nums)):   
            if nums[i] < m:
                m = nums[i]
        
        return m



        