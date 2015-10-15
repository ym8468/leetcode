class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        for x in range(1, m):
            grid[0][x] += grid[0][x-1]
        for y in range(1, n):
            grid[y][0] += grid[y-1][0]
        for y in range(1, n):
            for x in range(1, m):
                grid[y][x] += min(grid[y][x-1], grid[y-1][x])
        return grid[-1][-1]
