class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        longest = 0
        
        for n in nums:
            if (n-1) not in numS:
                length = 0
                while (n+length) in numS:
                    length+=1
                longest = max(longest,length)
        return longest

        