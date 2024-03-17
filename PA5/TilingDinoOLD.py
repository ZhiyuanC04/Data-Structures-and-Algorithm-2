# CS3100 - Fall 2023 - Programming Assignment 5
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
# Your Computing ID: vgs3qt
# Collaborators: yl2nr, bbh9ba
# Sources: Introduction to Algorithms, Cormen
#################################
from collections import deque

class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        # # Parse input and build a graph representation of the image
        # rows = len(lines)
        # cols = len(lines[0])
        # graph, node_id = {}, lambda r, c: r * cols + c
        #
        # for r in range(rows):
        #     for c in range(cols):
        #         if lines[r][c] == '#':
        #             graph[node_id(r, c)] = []
        #             for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        #                 nr, nc = r + dr, c + dc
        #                 if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '#':
        #                     graph[node_id(r, c)].append(node_id(nr, nc))
        #
        # # BFS to find augmenting paths
        # def bfs(source, sink, parent):
        #     visited, queue = set(), deque([source])
        #     while queue:
        #         node = queue.popleft()
        #         if node == sink:
        #             return True
        #         for neigh in graph.get(node, []):
        #             if neigh not in visited and neigh not in parent:
        #                 parent[neigh] = node
        #                 visited.add(neigh)
        #                 queue.append(neigh)
        #     return False
        #
        # # Ford-Fulkerson for max flow
        # def ford_fulkerson(source, sink):
        #     parent, max_flow = {}, 0
        #     while bfs(source, sink, parent):
        #         path_flow, v = float('inf'), sink
        #         while v != source:
        #             path_flow = min(path_flow, 1)
        #             v = parent[v]
        #         max_flow += path_flow
        #         v = sink
        #         while v != source:
        #             u = parent[v]
        #             graph[u].remove(v)
        #             graph[v].append(u)
        #             v = parent[v]
        #     return max_flow
        #
        # # Add source and sink
        # source, sink = -1, -2
        # for r in range(rows):
        #     for c in range(cols):
        #         if lines[r][c] == '#':
        #             if (r + c) % 2 == 0:
        #                 graph[source] = graph.get(source, []) + [node_id(r, c)]
        #             else:
        #                 graph[node_id(r, c)] = graph.get(node_id(r, c), []) + [sink]
        #
        # # Check if a perfect matching exists
        # if ford_fulkerson(source, sink) != sum(lines[r][c] == '#' for r in range(rows) for c in range(cols)) // 2:
        #     return ["impossible"]
        #
        # # Construct the tiling
        # tiling = []
        # for u in graph[source]:
        #     if u in parent:
        #         v = parent[u]
        #         r1, c1 = divmod(u, cols)
        #         r2, c2 = divmod(v, cols)
        #         tiling.append(f"{c1} {r1} {c2} {r2}")
        #
        # return tiling
        rows = len(lines)
        cols = len(lines[0])
        graph = {}
        node_id = lambda r, c: r * cols + c # Function that put 2-D into 1-D for graph.

        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == '#':
                    graph[node_id(r, c)] = [] # If this position is black, create the key.
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Check adjacent pixel for black ones.
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '#':
                            graph[node_id(r, c)].append(node_id(nr, nc)) # Append the coordinates of adjacent points.

        print("graph")
        print(graph)

        def bfs(source, sink, parent): # Find path from source to the sink.
            visited = set()
            queue = deque([source])

            print("queue")
            print(queue)

            while queue:
                node = queue.popleft() # First node in queue, the source is the first one to pop.
                if node == sink:
                    return True # End, found a path.
                for neighb in graph.get(node, []):
                    if neighb not in visited and neighb not in parent:
                        parent[neighb] = node
                        visited.add(neighb)
                        queue.append(neighb)
            return False

        def ford_fulkerson(source, sink):
            parent = {}
            max_flow = 0
            while bfs(source, sink, parent):
                path_flow = float('inf')
                v = sink
                while v != source:
                    path_flow = min(path_flow, 1)
                    v = parent[v]
                max_flow += path_flow
                v = sink
                while v != source:
                    u = parent[v]
                    graph[u].remove(v)
                    if u not in graph[v]:
                        graph[v].append(u)
                    v = parent[v]
            return max_flow

        source, sink = -1, -2
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == '#':
                    if (r + c) % 2 == 0:
                        graph[source] = graph.get(source, []) + [node_id(r, c)]
                    else:
                        graph[node_id(r, c)] = graph.get(node_id(r, c), []) + [sink]

        if ford_fulkerson(source, sink) != sum(lines[r][c] == '#' for r in range(rows) for c in range(cols)) // 2:
            return ["impossible"]

        tiling = []
        for u in graph[source]:
            if u in parent:
                v = parent[u]
                r1, c1 = divmod(u, cols)
                r2, c2 = divmod(v, cols)
                tiling.append(f"{c1} {r1} {c2} {r2}")

        return tiling