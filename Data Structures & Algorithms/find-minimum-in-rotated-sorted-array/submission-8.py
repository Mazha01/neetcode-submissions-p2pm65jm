class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1 

        res = nums[0]

        while l <=r:
            if nums[l] <  nums[r]:
               res = min(res, nums[l])
               break

            m = l + (r - l) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1     
            

        return res
        
        
#  [2, 3, 4,5,6,7,8,9,10, 11, 12, 13,14,15,16,17,18,19,20, 1]   