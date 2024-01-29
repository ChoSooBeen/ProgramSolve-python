from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def bfs(x, y) :
            queue = deque()

            grid[x][y] = "2"
            queue.append([x, y])

            while queue :
                cur = queue.popleft()
                for d in dir :
                    nx = cur[0] + d[0]
                    ny = cur[1] + d[1]
                    if nx >= 0 and ny >= 0 and nx < row and ny < col and grid[nx][ny] == "1" :
                        grid[nx][ny] = "2"
                        queue.append([nx, ny])

        count = 0
        for i in range(row) :
            for j in range(col) :
                if grid[i][j] == "1" :
                    bfs(i, j)
                    count += 1
        return count