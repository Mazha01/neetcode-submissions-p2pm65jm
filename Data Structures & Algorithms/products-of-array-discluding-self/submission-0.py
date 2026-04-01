class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            resNum = 1
            for j in range(len(nums)):
                if i!=j:
                    resNum = resNum * nums[j]
            res.append(resNum)

        return res    