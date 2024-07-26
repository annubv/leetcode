"""
1926. Nearest Exit from Entrance in Maze
Medium
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Amazon
2
"""

from collections import deque

DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        q = deque([])

        q.append(entrance)

        maze[entrance[0]][entrance[1]] = "+"
        steps = 0

        while q:
            qn = len(q)
            for i in range(qn):
                new_item = q.popleft()
                i = new_item[0]
                j = new_item[1]                
                
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and not (i==entrance[0] and j==entrance[1]):
                    return steps

                for d in DIRS:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if new_i > -1 and new_i < n and new_j > -1 and new_j < m and maze[new_i][new_j] != "+":
                        q.append([new_i, new_j])
                        maze[new_i][new_j] = "+"

            steps += 1


        return -1
