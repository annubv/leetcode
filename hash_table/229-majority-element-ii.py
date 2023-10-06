"""
229. Majority Element II
Medium

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Amazon
4
Microsoft
3
Adobe
2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        num1 = float(-inf)
        num2 = float(-inf)
        c1 = 0
        c2 = 0
        n = len(nums)/3

        for i in nums:
            if i == num1:
                c1 += 1
            elif i == num2:
                c2 += 1
            elif c1 == 0:
                num1 = i
                c1 = 1
            elif c2 == 0:
                num2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1


        cc1 = 0
        cc2 = 0

        for i in nums:
            if i == num1:
                cc1 += 1
            elif i == num2:
                cc2 += 1

        result = []
        if cc1 > n:
            result.append(num1)
        if cc2 > n:
            result.append(num2) 
        
        return result