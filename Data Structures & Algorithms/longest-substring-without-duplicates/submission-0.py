class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL = 0
        sets = set()

        for r in range(len(s)):
            while s[r] in sets:
                sets.remove(s[l])
                l+=1

            sets.add(s[r])
            maxL = max(maxL,r-l+1)
        return maxL
    
            
        

        
                
        
        
        