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

import networkx as network


class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling.
    #
    # @return the list of strings representing the tiling.

    def compute(self, lines):

        # Number of rows.
        rows = len(lines)
        # Number of columns.
        cols = len(lines[0])

        # Creating the Graph using networkx package.
        Graph = network.DiGraph()

        # Define source and sink.
        source = 'source'
        sink = 'sink'

        # Build the graph.
        for r in range(rows):
            for c in range(cols):
                # Loop row by row.
                # Loop all elements from input and check for black pixel (#).
                if lines[r][c] == '#':
                    node = (r, c)
                    # Create a bipartite graph.
                    if (r + c) % 2 == 0:
                        Graph.add_edge(source, node, capacity=1)
                    else:
                        Graph.add_edge(node, sink, capacity=1)
                    # Add edges for adjacent black pixels.
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '#':
                            # Check if the node is in Set A.
                            # We only connect nodes from Set A to nodes in Set B.
                            if (r + c) % 2 == 0:
                                Graph.add_edge(node, (nr, nc), capacity=1)

        # Compute the maximum flow.
        flow_value, flow_dict = network.maximum_flow(Graph, source, sink)
        # Flow_value holds the total flow value
        # Flow_dict contains the flow details across individual edges.

        # Check if a perfect matching exists.
        # Each donimo covers two black pixels, so we divided the total number by 2.
        if flow_value != sum(lines[r][c] == '#' for r in range(rows) for c in range(cols)) // 2:
            return ["impossible"]

        # Construct the tiling.
        tiling = []
        # Get all connected node from source.
        for u in flow_dict[source]:
            # Check the capacity part (1). 1 means there is a domino.
            if flow_dict[source][u] > 0:
                # For all nodes connect to u. Check adjacent nodes.
                for v in flow_dict[u]:
                    # Check if there is a positive flow (1) to v.
                    # Positive means v in Set B is the other end of the domino.
                    if flow_dict[u][v] > 0:
                        # Put the corresponding coordinates into the array.
                        r1, c1 = v
                        r2, c2 = u
                        tiling.append(f"{c1} {r1} {c2} {r2}")
        return tiling