"""
208. Implement Trie (Prefix Tree)

Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and
retrieve keys in a dataset of strings. There are various applications of this data structure, such as
autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word
that has the prefix prefix, and false otherwise.

Amazon
15
Google
9
Twitter
6
Microsoft
5
Snapchat
4
Apple
3
Facebook
2
Oracle
2
ByteDance
2
"""


class TrieNode:
    def __init__(self):
        self.is_word_end = False
        self.children = [None for _ in range(26)]


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        pointer = self.root
        for char in word:
            char_idx = ord(char)-ord("a")
            if pointer.children[char_idx] is None:
                pointer.children[char_idx] = TrieNode()
            pointer = pointer.children[char_idx]
        pointer.is_word_end = True


    def search(self, word: str) -> bool:
        pointer = self.root
        for char in word:
            char_idx = ord(char)-ord("a")
            if pointer.children[char_idx] is None:
                return False
            pointer = pointer.children[char_idx]
        return pointer.is_word_end
        

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for char in prefix:
            char_idx = ord(char)-ord("a")
            if pointer.children[char_idx] is None:
                return False
            pointer = pointer.children[char_idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)