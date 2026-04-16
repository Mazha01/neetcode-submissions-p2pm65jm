class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 4
        r = max(piles) 
        # 2
        l = math.ceil(sum(piles)/h)

        # 4
        min_v = len(piles)

        # [1,4,3,2]
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile/m)

            if t > h:
                l = m +1
            elif  t <= h:
                res = m
                r = m - 1
         

        return res