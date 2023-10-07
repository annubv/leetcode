"""
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

Hard

You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:
You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.


"""


M = pow(10, 9) + 7

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = dict()
        def solve(index, search_cost, current_max):
            if index in dp and search_cost in dp[index] and current_max in dp[index][search_cost]:
                return dp[index][search_cost][current_max]

            if index == n:
                if search_cost == k:
                    return 1
                else:
                    return 0

            result = 0
            for i in range(1, m+1):
                if i > current_max:
                    result += solve(index+1, search_cost+1, i)
                else:
                    result += solve(index+1, search_cost, current_max)

            result = result%M

            if index not in dp:
                dp[index] = dict()

            if search_cost not in dp[index]:
                 dp[index][search_cost] = dict()

            dp[index][search_cost][current_max] = result
            return result
        
        return solve(0, 0, -1)