class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mc = Counter(nums)

        return [key for key,value in mc.most_common(k)]
        


        