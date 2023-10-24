"""
215. Kth Largest Element in an Array

Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.


Facebook
140
Amazon
16
LinkedIn
14
Microsoft
12
Google
8
Bloomberg
5
Adobe
5
tiktok
3
Goldman Sachs
2

"""



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > k:
                heapq.heappop(pq)
            
        return pq[0]