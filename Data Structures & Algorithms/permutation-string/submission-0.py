class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        target = Counter(s1)

        for i in range(len(s2) - n + 1):
            window = Counter(s2[i:i+n])

            if window == target:
                return True

        return False