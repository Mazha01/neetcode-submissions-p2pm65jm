class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l  = 0
        # max_price = 0
    
        # while l < r:
        #     while l < r:
        #         price = prices[r] - prices[l] 
        #         print(price)
        #         max_price = max(max_price, price)
        #         r-=1
        #     r = len(prices)-1
        #     l+=1
        # return max_price

        l  = 0
        max_price = 0

        for r in range(1, len(prices)):
            if prices[r]>prices[l]:
              max_price = max(max_price, prices[r]-prices[l])
            else:
                l = r  

        return  max_price     




