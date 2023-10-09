"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lm, rm = -1, -1
        
        # FIRST SEARCH FOR LEFTMOST NUM

        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] > target:
                r = mid-1
            
            elif nums[mid] < target:
                l = mid + 1

            else:
                lm = mid
                r = mid - 1        

        # THEN SEARCH FOR RIGHTMOST NUM

        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l+r)//2

            if nums[mid] > target:
                r = mid-1
            
            elif nums[mid] < target:
                l = mid + 1

            else:
                rm = mid
                l = mid + 1        


        return [lm, rm]