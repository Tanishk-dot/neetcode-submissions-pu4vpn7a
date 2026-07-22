class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i:[] for i in range(n)}
        visit = set()
        for csr,pre in edges:
            preMap[csr].append(pre)
            preMap[pre].append(csr)

        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for nei in preMap[i]:
                dfs(nei)

        count = 0 
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        return count
       
        
        



        