"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
"""

from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # get the size of graph
        n = len(graph)
        
        if n <= 1:
            return 0

        # initialize queue and visited set for BFS
        que = deque([]) # This will have pair of node and its mask
        visited = set() # This will have pair of node and its mask


        # BFS from all nodes, means push every node into the queue

        for i in range(n):
            mask_value = 1 << i
            que.append((i, mask_value))
            # also mark it as visited
            visited.add((i, mask_value))

        
        """
        all_visited_state denotes the state when all the nodes
        are marked as visited
        """
        all_visited_state = (1 << n) - 1 # 1111
        path = 0

        # start the BFS
        while que:
            # remove all the nodes first to get all the nodes
            # from the current level

            que_size = len(que)
            path += 1

            while(que_size):
                que_size -= 1
                curr = que.popleft()

                curr_node = curr[0]
                curr_mask = curr[1]

                for v in graph[curr_node]:
                    # get all the nodes the current node can visit to
                    next_mask = curr_mask | (1 << v)

                    if next_mask == all_visited_state:
                        # case when the mask is 1111
                        return path

                    if (v, next_mask) not in visited:
                        # if the node is not already visited, lets visit that
                        que.append((v, next_mask))
                        visited.add((v, next_mask))
            
        return -1

        