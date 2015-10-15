class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        sin = set([])
        tri = set([])
        for i in nums:
            if i in tri:
                continue
            elif i in sin:
                sin.remove(i)
                tri.add(i)
            else:
                sin.add(i)
        return sin.pop()
