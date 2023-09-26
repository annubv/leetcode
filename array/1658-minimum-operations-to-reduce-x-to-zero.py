"""
1658. Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.


Google
3
Amazon
2
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
      n = len(nums)
      sum_map = {0 : -1}

      curr_sum = 0
      for i in range(n):
        curr_sum += nums[i]
        sum_map[curr_sum] = i

      y = curr_sum-x
      result = -1
      curr_sum = 0
      for i in range(n):
        curr_sum += nums[i]

        required_sum = curr_sum - y
        if required_sum in sum_map:
          k = sum_map[required_sum]
          result=max(result, i-k)

      return -1 if result == -1 else n-result
