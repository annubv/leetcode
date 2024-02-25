"""
5. Longest Palindromic Substring

Medium

Given a string s, return the longest 
palindromic substring in s.

Amazon
35
Microsoft
18
Google
12
Adobe
12
Facebook
7
Apple
7
Oracle
7
Bloomberg
6
Goldman Sachs

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:   
        
        def expand(i, j):
            l = i
            r = j

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return r-l-1

        start = 0
        end = 0
        
        for i in range(len(s)):
            odd_pali  = expand(i, i)
            if odd_pali > end - start + 1:
                dist = odd_pali//2
                start = i-dist
                end = i+dist

            even_pali = expand(i, i+1)
            if even_pali > end - start + 1:
                dist = even_pali//2 - 1
                start = i-dist
                end = i+dist+1
        
        return s[start:end+1]