class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols= len(grid),len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        def addRoom(r,c):
            nonlocal fresh
            if( r < 0 or c < 0 or r >=rows or c >= cols or grid[r][c] != 1 or (r,c) in visit):
                return
            q.append([r,c])
            visit.add((r,c))
            fresh -=1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))

        count = 0
        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            count += 1
        return count if fresh == 0 else -1
            
        
        