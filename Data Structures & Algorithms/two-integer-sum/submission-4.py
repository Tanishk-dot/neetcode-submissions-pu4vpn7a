class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i , num in enumerate(nums):
            j = target - num
            if j in hashmap:
                return [hashmap[j], i]

            hashmap[num] = i
       
        

        
        