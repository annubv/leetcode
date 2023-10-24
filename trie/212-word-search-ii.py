"""
212. Word Search II

Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Uber
36
Amazon
31
Cisco
16
Microsoft
7
Facebook
5
Snapchat
5
Google
5
Twitter
5
Karat
5
Apple
4
"""

DIRS = ((0,1), (1,0), (-1, 0), (0, -1))

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word_end = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        def insert_word_in_trie(word):
            pointer = root
            for char in word:
                idx = ord(char)-ord("a")
                if pointer.children[idx] is None:
                    pointer.children[idx] = TrieNode()
                pointer = pointer.children[idx]
            
            pointer.is_word_end = True
            pointer.word = word

        
        for word in words:
            insert_word_in_trie(word)


        ans = []
        n = len(board)
        m = len(board[0])

        def solve(i, j, trie_node):
            if i<0 or j<0 or i>=n or j>=m or board[i][j] == ".":
                return False
            
            char = board[i][j]
            char_idx = ord(char) - ord("a")

            new_trie_node = trie_node.children[char_idx]
            if new_trie_node is None:
                return False

            if new_trie_node.is_word_end:
                ans.append(new_trie_node.word)
            
            new_trie_node.is_word_end = False

            board[i][j] = "."

            for d in DIRS:
                solve(i+d[0], j+d[1], new_trie_node)
            
            board[i][j] = char

        for i in range(n):
            for j in range(m):
                solve(i,j,root)


        return ans








