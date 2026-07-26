class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1,-1,-1):
            nextp = set()
            for t in dp:
                nextp.add(t + nums[i])
                nextp.add(t)

            dp = nextp
        return True if target in dp else False
        