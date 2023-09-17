"""
Hard

6 months - 1 year
Netflix 8
Bloomberg 5
Google 3
Uber 3
Facebook 2
Amazon 2
1 year - 2 years
Media.net 16
Twitter 4
Directi 4
JPMorgan 3
Twilio 2
Apple 2
DoorDash 2
Citadel 2
Walmart Labs 2


You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
"""
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # make adjacency list
        n = len(tickets)
        adj = defaultdict(list)
        for t in tickets:
            u = t[0]
            v = t[1]
            adj[u].append(v)
        

        # sorting in lexical order
        for i in adj:
            adj[i].sort()
        
        def solve(u, arg_path):
            arg_path.append(u)

            if len(arg_path) == n + 1:
                self.result = arg_path
                return True
            
            neighbor_cities = adj[u]
            for i in range(len(adj[u])):
                to_city = adj[u][i]
                if to_city:
                    adj[u][i] = ""
                    if solve(to_city, arg_path):
                        return True
                    else:
                        adj[u][i] = to_city    
            arg_path.pop()
            return False

    
        solve("JFK", [])

        return self.result