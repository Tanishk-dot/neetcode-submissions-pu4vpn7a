class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            j = target - num
            if j in mp:
                return [mp[j],i]

            mp[num] = i
        
        

        
        