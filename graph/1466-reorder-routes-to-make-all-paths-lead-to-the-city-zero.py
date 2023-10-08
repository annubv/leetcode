"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

Medium

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

DRW
4
Amazon
3
American Express
3
Grab
2

"""

class Solution:
    def __init__(self):
        self.ans = 0 

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = [[] for i in range(n)]
        for i in connections:
            adj_list[i[0]].append((i[1], 1))
            adj_list[i[1]].append((i[0], 0))

        def dfs(node, parent):
            for pair in adj_list[node]:
                v = pair[0]
                check = pair[1]
                if v!=parent:
                    if check == 1:
                        self.ans += 1
                    dfs(v, node)

        dfs(0, -1)
        return self.ans
