from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for ch in s:
            count[ch] +=1

        for ch in t:
            count[ch] -=1

        for val in count.values():
            if val != 0:
                return False

        return True        


        