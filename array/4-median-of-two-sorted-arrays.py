"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Amazon
40
Adobe
19
Goldman Sachs
18
Microsoft
15
Apple
15
Google
14
Facebook
7
ServiceNow
4
Paypal
3
Bloomberg
2
VMware
2
LinkedIn
2
Walmart Global Tech
2
Yandex
2



O(min(m,n))
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)

        l = 0
        r = m

        while l <= r:
            px = l + (r-l)//2
            py = (m+n+1)//2 - px
            
            # LEFT SIDE ELEMENTS
            x1 = float(-inf) if px == 0 else nums1[px-1]
            x2 =  float(-inf) if py == 0 else nums2[py-1]

            # RIGHT SIDE ELEMENTS
            x3 = float(inf) if px == m else nums1[px]
            x4 =  float(inf) if py == n else nums2[py]

            if x1 <= x4 and x2 <= x3:
                if (m+n)%2 == 0:
                    return (max(x1, x2) + min(x3, x4))/2
                return max(x1, x2)
            
            if x1 > x4:
                r = px - 1
            else:
                l = px + 1

        return -1