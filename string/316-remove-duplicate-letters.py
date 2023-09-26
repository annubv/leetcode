"""
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

Apple
4
Facebook
2
Amazon
2
Salesforce
2

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mapper = dict()
        seen = dict()

        for idx, i in enumerate(s):
            mapper[i] = idx

        result = []
        for idx, c in enumerate(s):
            if seen.get(c):
                continue
            while result and result[-1] >= c and mapper[result[-1]] > idx:
                seen[result[-1]] = False
                result.pop()
            result.append(c)
            seen[c] = True
        return "".join(result)
