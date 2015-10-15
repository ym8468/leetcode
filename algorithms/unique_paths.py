class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1 for col in range(m)] for row in range(n)]
        for y in range(1, n):
            for x in range(1, m):
                grid[y][x] = grid[y-1][x] + grid[y][x-1]
        return grid[-1][-1]
