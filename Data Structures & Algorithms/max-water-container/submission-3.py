class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_ar = 0
        while left < right:
            ar = min(heights[left],heights[right]) * (right-left)
            max_ar = max(ar,max_ar)

            if heights[left] < heights[right] : 
                left+=1

            else:
                right -=1

        return max_ar
        

        