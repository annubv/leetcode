"""
1268. Search Suggestions System

Medium

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Amazon
68
Google
3
Facebook
3
Oracle
3
Apple
2
Adobe
2
"""

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word_end = False
        self.word = ""

class Solution:
    def __init__(self):
        self.max_product_length = 0

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()

        def insert_word(word):
            self.max_product_length = max(self.max_product_length, len(word))

            pointer = root
            for char in word:
                char_idx = ord(char)-ord("a")
                if pointer.children[char_idx] is None:
                    pointer.children[char_idx] = TrieNode()
                pointer = pointer.children[char_idx]
            
            pointer.is_word_end = True
            pointer.word = word


        for product in products:
            insert_word(product)


        result = []

        def search_in_trie(word) -> List[str]:
            current_result = []

            if len(word) > self.max_product_length:
                return current_result

            # GET TO THE NODE WHERE MY word ENDS

            pointer = root
            for char in word:
                char_idx = ord(char)-ord("a")
                if pointer.children[char_idx] is None:
                    return current_result
                pointer = pointer.children[char_idx]

            
            def append_word_with_dfs(current_node, current_word, current_result):
                if len(current_result) == 3:
                    return             
                if current_node.is_word_end:
                    current_result.append(current_node.word)                
                for i in range(26):
                    c = current_node.children[i]
                    if c is not None:
                        current_word += chr(i+ord("a"))
                        append_word_with_dfs(c, current_word, current_result)
                        current_word = current_word[:-1]

            append_word_with_dfs(pointer, word, current_result)
            return current_result

        n = len(searchWord)
        for i in range(1, n+1):
            current_word = searchWord[:i]
            result.append(search_in_trie(current_word))
        
        return result


