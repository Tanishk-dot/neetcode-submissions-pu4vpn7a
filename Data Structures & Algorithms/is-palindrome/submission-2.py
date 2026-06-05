class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = "".join(filter(str.isalnum,s))
        return s1 == s1[::-1]
        