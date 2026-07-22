class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(1,len(edges)+1)}

        visit = set()
        def dfs(src,target):
            if src == target:
                return True

            visit.add(src)
            for nei in graph[src]:
                if nei not in visit:
                    if dfs(nei,target):
                        return True
            return False

        for u,v in edges:
            visit = set()

            if dfs(u,v):
                return [u,v]

            graph[u].append(v)
            graph[v].append(u)


        