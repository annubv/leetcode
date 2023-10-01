"""

557. Reverse Words in a String III

Easy

Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

Microsoft
5
Amazon
3
Bolt
3
Yandex
2
Facebook
2
Apple
2
PayTM
2
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        current_word = ""
        n = len(s)

        for i in range(n-1, -1, -1):
            current_character = s[i]

            if s[i] == " ":
                current_word = " "+current_word
                result = current_word+result
                current_word = ""

            else:
                current_word += current_character
        
        return current_word+result
