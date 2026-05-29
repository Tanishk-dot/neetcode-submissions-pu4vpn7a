from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for ch in nums:
            count[ch] += 1

        for values in count.values():
            if values > 1:
                return True 

        return False

        

        
            
    
        
        