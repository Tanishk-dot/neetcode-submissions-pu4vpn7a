class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        a,b = 0,0
        for n in nums:
            temp = max(a+n,b)
            a = b
            b = temp
        return b


        