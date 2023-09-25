"""
389. Find the Difference

You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

Google
6
Amazon
3
Apple
2
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum([ord(i) for i in s])
        t_sum = sum([ord(i) for i in t])
        return chr(t_sum - s_sum)
