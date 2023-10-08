"""
399. Evaluate Division

Medium

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.\

Uber
14
Amazon
10
Google
8
Facebook
8
Snapchat
5
tiktok
4
Adobe
3
Bloomberg
2
BlackRock
2
"""

class Solution:
    def __init__(self):
        self.ans = -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        adj = defaultdict(list)

        for i in range(n):
            pair = equations[i]
            src = pair[0]
            dst = pair[1]
            wt = values[i]
            adj[src].append((dst, wt)) # a/b
            adj[dst].append((src, 1/wt)) # b/a

        def dfs(node, dst, visited, product):

            if node in visited:
                return

            visited.add(node)

            if node == dst:
                self.ans = product
                return


            for pair in adj[node]:
                new_node = pair[0]
                wt = pair[1]
                dfs(new_node, dst, visited, product*wt)


        result = []
        for query in queries:
            src = query[0]
            dst = query[1]

            if src not in adj or dst not in adj:
                result.append(-1)

            else:
                self.ans = -1
                product = 1

                visited = set()
                dfs(src, dst, visited, product)

                result.append(self.ans)

        return result