class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        print(nums_set)
        longest = 0

        for num in nums:
            count = 0
            if num-1 not in nums_set:
                count = 1
                cur = num
                while cur+1 in nums_set:
                    cur +=1
                    count+=1
            longest = max(longest, count) 

        return   longest   


                

          
        