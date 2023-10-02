"""
2038. Remove Colored Pieces if Both Neighbors are the Same Color

There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

Walmart Global Tech 9

"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_turns = 0
        b_turns = 0


        i = 1
        n = len(colors) - 1
        while i < n:
            if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
                a_turns += 1
            if colors[i] == "B" and colors[i-1] == "B" and colors[i+1] == "B":
                b_turns += 1
            i += 1

        return a_turns > b_turns
