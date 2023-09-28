"""
905. Sort Array By Parity

Easy

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            while i < j and nums[i]%2 == 0:
                i += 1
            while i < j and nums[j]%2 == 1:
                j -= 1
            nums[i], nums[j] = nums[j] , nums[i]
        return nums