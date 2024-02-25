"""
2709. Greatest Common Divisor Traversal
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.
Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.
Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
"""

class Dsu:
    def __init__(self, n):
        self.comp_count = n
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        ans = self.find(self.parents[x])
        self.parents[x] = ans
        return ans

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.size[x_parent] > self.size[y_parent]:
            self.parents[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        else:
            self.parents[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]

        self.comp_count -= 1

    def get_comp_count(self):
        return self.comp_count


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = Dsu(n=n)

        fac_idx = dict()

        for i in range(n):
            factor = 2
            while factor*factor <= nums[i]:
                if nums[i]%factor==0:
                    if factor in fac_idx:
                        idx = fac_idx[factor]
                        dsu.union(idx, i)
                    else:
                        fac_idx[factor] = i

                    while nums[i]%factor == 0:
                        nums[i] = nums[i]//factor
                
                factor+=1

            if nums[i] > 1:
                factor = nums[i]
                if factor in fac_idx:
                    idx = fac_idx[factor]
                    dsu.union(idx, i)
                else:
                    fac_idx[factor] = i

        
        return dsu.get_comp_count() == 1