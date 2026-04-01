class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # for i in range(len(nums)):
        #     resNum = 1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             resNum = resNum * nums[j]
        #     res.append(resNum)

        # return res

        # 1 , 2 , 4, 5 input

        # 1, 2, 8, 48 prefix
        # 48, 48, 24, 6  sufix

        # 48, 24, 12, 8  output

        # prefix = []
        # sufix = []
        # res = [0] * len(nums)

        # num = 1

        # for i in range(len(nums)):
        #    num = nums[i] * num
        #    prefix.append(num)


        # num = 1
        # for i in range(len(nums)-1, -1, -1):
        #     num = nums[i] * num
        #     sufix.insert(0, num)

 
        # print(prefix)
        # print(sufix)       

        # for i in range(len(nums)):
        #     if i == 0:
        #         res[i] = 1 * sufix[i+1] 
        #     elif i == len(nums)-1:
        #         res[i] = prefix[i-1] * 1
        #     else:   
        #          res[i]=sufix[i+1] * prefix[i-1] 

        # return res       

        prefix = 1
        sufix = 1
        res=[0]*len(nums)
        n= len(nums)
        
        for i in range(n):
           res[i]=prefix
           prefix*=nums[i]

        for i in range(n-1,-1,-1):
            res[i] = res[i]*sufix
            sufix*=nums[i]

        return  res  



