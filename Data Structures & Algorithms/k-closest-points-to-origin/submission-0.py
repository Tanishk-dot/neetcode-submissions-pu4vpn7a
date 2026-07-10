class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for [i,j] in points:
            dist.append((i*i + j*j , [i,j]))

        heapq.heapify(dist)
        res = []
        for _ in range(k):
            d,point = heapq.heappop(dist)
            res.append(point)
        return res
            
        