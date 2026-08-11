class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxl = 0
        while l < r:
            arr = min(heights[l],heights[r])*(r-l)
            if heights[l] < heights[r]:
                l += 1

            else:
                r-= 1

            maxl = max(maxl,arr)
        return maxl

            
        

        