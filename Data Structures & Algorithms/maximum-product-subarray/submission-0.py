class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin = nums[0]
        cmax = nums[0]
        res = nums[0]

        for num in nums[1:]:
            if num < 0:
                cmin,cmax = cmax,cmin

            cmax = max(num,cmax*num)
            cmin = min(num,cmin*num)
            res = max(res,cmax)

        return res

        