class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        visit = set()
        res = []

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs): 
            nonlocal res
            if crs in visit:
                return False
            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return []
            visit.remove(crs)
            preMap[crs] = []
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return res
        