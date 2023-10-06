"""
343. Integer Break

Medium

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Facebook
3
"""


# DP SOLUTION TC: O(n^2), SC: O(n)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = dict()

        def solve(x):
            if x == 1:
                return 1
            if x in dp:
                return dp[x]

            result = -1

            for i in range(1, x):
                product = i * max(x-i, solve(x-i))
                result = max(product, result)

            dp[x] = result
            return dp[x]

        return solve(n)

# MATH SOLUTION TC: O(1), SC: O(1)
class Solution2:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        q = n // 3
        r = n % 3
        if r == 0:
            return int((math.pow(3, q)))
        elif r == 1:
            return int((math.pow(3, (q-1))) * 4)
        else:
            return int((math.pow(3, q)) * 2)