# CS3100 - Fall 2023 - Programming Assignment 3
#################################
# Collaboration Policy: You may discuss the problem and the overall
# strategy with up to 4 other students, but you MUST list those people
# in your submission under collaborators.  You may NOT share code,
# look at others' code, or help others debug their code.  Please read
# the syllabus carefully around coding.  Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: Zhiyuan Chang (vgs3qt)
# Collaborators: Yining Liu(yl2nr), Yuhao Niu(bhb9ba)
# Sources: Introduction to Algorithms, Cormen
#################################

import heapq as pq

class Clustering:
    def __init__(self):
        return

     # This is the method that should compute the maximum possible
     # spacing. It takes as input an integer k and an nxn array of
     # distances. 
     #
     # @return the maximum possible spacing

    def compute(self, k, distances):
        # We don't really care about the node, we record it becasue we want to check if all nodes are seen.
        # We also don't need the graph so we sort all the weight from prim's algorithm and remove those that is cut.
        priority_queue = []
        seen = set()
        result = []
        n = len(distances)

        seen.add(0)
        for j in range(1, n): # Push the node 0 and distance to other node into the queue.
            if distances[0][j] != 0:
            # Pusb distance to other node into the quese, it is a heap so it sort the distance.
                pq.heappush(priority_queue, (distances[0][j], 0, j))

        while len(seen) < n:
            weight, u, v = pq.heappop(priority_queue) # pop the lowest distance out.
            if v not in seen:
                seen.add(v)
                result.append(weight)
            for j in range(n):
                if distances[v][j] != 0 and j not in seen:
                    pq.heappush(priority_queue, (distances[v][j], v, j))

        result.sort(reverse=True) # Sort on descending order.
        for i in range(k - 2): # Cut the graph into k clusters.
            result.pop(0)   # Check the minimum distance between clusters.
        return result[0]