"""
1458. Max Dot Product of Two Subsequences

Hard

Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
"""


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = defaultdict(dict)
        n = len(nums1)
        m = len(nums2)

        def solve(i, j):
            if i == n or j == m:
                return float(-inf)

            if i in dp and j in dp[i]:
                return dp[i][j]

            p1 = nums1[i] * nums2[j]
            p2 = (nums1[i] * nums2[j]) + solve(i+1, j+1)
            p3 = solve(i, j+1)
            p4 = solve(i+1, j)

            ans = max(p1, p2, p3, p4)

            dp[i][j] = ans
            return ans

        return solve(0, 0)
