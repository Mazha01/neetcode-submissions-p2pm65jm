class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0
        while l <r:
            x = r -l
            if heights[l]>heights[r]:
                area = max(area, heights[r]*x)
                r-=1
            else:
                area=max(area,heights[l]*x)
                l+=1
        return area

