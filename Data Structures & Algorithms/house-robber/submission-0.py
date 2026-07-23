class Solution:
    def rob(self, nums: List[int]) -> int:
        
        for r in range(len(nums) -3,-1,-1):
            max_rob = []
            for i in range(r+2,len(nums)):
                max_rob.append(nums[i])
            nums[r] += max(max_rob)

        return max(nums)

        