class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        edges = [i*i for i in range(1, int(n**0.5)+1)]
        edgesCount = len(edges)
        visited = [False] * (n+1)
        level = 0
        children = {0:0}
        while True:
            level += 1
            parents = children
            children = {}
            for parentV in parents:
                startIndex = parents[parentV]
                for edgeIndex in range(startIndex, edgesCount):
                    childV = parentV + edges[edgeIndex]
                    if childV == n:
                        return level
                    if childV > n:
                        break
                    if visited[childV]:
                        continue
                    visited[childV] = True
                    child = {childV:edgeIndex}
                    children.update(child)
