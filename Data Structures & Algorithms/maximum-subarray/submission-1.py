class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currsum = 0

        for num in nums:
            if currsum < 0:
                currsum = 0

            currsum += num
            maxsub = max(maxsub,currsum)

        return maxsub
        

        