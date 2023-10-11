"""
295. Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 
"""


class MedianFinder:
    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
        
    def addNum(self, num: int) -> None:
        if not self.left_max_heap or num > self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, num)
        else:
            heapq.heappush(self.right_min_heap, -1*num)

        if len(self.left_max_heap) - len(self.right_min_heap) > 1:
            item = heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, -1*item)
    
        elif len(self.right_min_heap) > len(self.left_max_heap):
            item = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -1*item)

    
    def findMedian(self) -> float:
        if len(self.left_max_heap) == len(self.right_min_heap):
            i = self.left_max_heap[0]
            j = -1 * self.right_min_heap[0]
            return (i+j)/2
        return self.left_max_heap[0]    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()