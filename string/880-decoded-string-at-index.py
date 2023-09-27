"""
880. Decoded String at Index

Medium

You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

Amazon 2

"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_size = 0
        n = len(s)

        for cc in s:
            if cc.isalpha():
                total_size += 1
            else:
                total_size *= int(cc)

        i = n-1
        while i >= 0:
            k %= total_size
            if k == 0 and s[i].isalpha():
                return s[i]
            elif s[i].isalpha():
                total_size -= 1
            else:
                total_size /= int(s[i])

            i -= 1

        return ""