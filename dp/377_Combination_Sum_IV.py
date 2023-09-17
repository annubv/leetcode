"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(dict)
        n = len(nums)

        def solve(i):
            # Returns n if there are n possible ways to reach target from the current number (i)
            if i in dp:
                return dp[i]

            if i == target:
                dp[i] = 1
                return 1

            if i > target:
                return 0

            res = 0
            for j in nums:
                res+=solve(i+j)

            dp[i] = res 
            return dp[i]

        return solve(0)
        

