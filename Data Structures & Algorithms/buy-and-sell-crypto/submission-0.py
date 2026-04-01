class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = len(prices)-1
        l  = 0
        max_price = 0
    
        while l < r:
            while l < r:
                price = prices[r] - prices[l] 
                print(price)
                max_price = max(max_price, price)
                r-=1
            r = len(prices)-1
            l+=1
        return max_price
