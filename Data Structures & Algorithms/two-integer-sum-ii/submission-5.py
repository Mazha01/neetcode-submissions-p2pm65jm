class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # srart_r =len(numbers)-1

        # for i in range(len(numbers)):
        #     while i < srart_r:
        #         if numbers[i]+numbers[srart_r] == target:
        #             return [i+1, srart_r+1]
        #         srart_r-=1    

        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[l]+numbers[r] > target:
                r-=1
            elif numbers[l]+numbers[r] < target:
                l+=1
            else:
                return[l+1, r+1]    

        

        return [0, 0]