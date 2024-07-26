"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
Solved
Medium
Topics
Companies
Hint
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

"""


class Solution:
    def dijkstra(self, n, adj, res, u):
        pq = []
        heapq.heappush(pq, (0, u))
        for i in range(len(res)):
            res[i] = float('inf')
        res[u] = 0

        while pq:
            ele = heapq.heappop(pq)
            d = ele[0]
            node = ele[1]

            for vec in adj[node]:
                v = vec[0]
                wt = vec[1]

                if d + wt < res[v]:
                    res[v] = d+wt
                    heapq.heappush(pq, (d+wt, v))

    def floydWarshall(self, n, fwspm):
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    fwspm[i][j] = min(fwspm[i][j], fwspm[i][via] + fwspm[via][j])

    def findRes(self, spm, n, distanceThreshold):
        rescity = -1
        resCount = float('inf')

        for i in range(n):
            c = 0
            for j in range(n):
                if i!=j and spm[i][j] <= distanceThreshold:
                    c += 1
            
            if c <= resCount:
                rescity = i
                resCount = c

        return rescity

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)

        fwspm = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            fwspm[i][i] = 0

        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            adj[u].append((v,w))
            adj[v].append((u,w))

            fwspm[u][v]  = w
            fwspm[v][u]  = w

        spm = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            spm[i][i] = 0

        # for i in range(n):
        #     self.dijkstra(n, adj, spm[i], i)
        # return self.findRes(spm, n, distanceThreshold)

        self.floydWarshall(n, fwspm)

        return self.findRes(fwspm, n, distanceThreshold)