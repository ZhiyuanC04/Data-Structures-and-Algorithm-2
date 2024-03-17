# CS3100 - Fall 2023 - Programming Assignment 4
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
import math

class SeamCarving:
    def __init__(self):
        self.seam = []
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def compute(self, image):
        ytotal = len(image)
        xtotal = len(image[0])
        min_e_map = []
        trace = []
        for b in range(ytotal):
            min_e_map.append([])
            trace.append([])
        for b in range(ytotal):
            for a in range(xtotal):
                min_e_map[b].append(None)
                trace[b].append(None)

        def Energy(y, x):
            neighbor = 0.0
            total = 0.0
            for i in [y - 1, y, y + 1]: # Loop through neighbors.
                for j in [x - 1, x, x + 1]:
                    if i == y and j == x: # Itself.
                        continue
                    if i < 0 or j < 0 or i >= ytotal or j >= xtotal: # Edge cases.
                        continue
                    red = (image[y][x][0] - image[i][j][0]) ** 2
                    green = (image[y][x][1] - image[i][j][1]) ** 2
                    blue = (image[y][x][2] - image[i][j][2]) ** 2
                    total += math.sqrt(red + green + blue) # Algorithm.
                    neighbor += 1
            energy = total / neighbor
            return energy

        def MinEnergyMap(y, x):
            # Bottom-up approach to build the table and update the trace.
            if y == ytotal - 1:
                min_e_map[y][x] = Energy(y, x) # If bottom row, energy is itself.
                return
            else:
                minimum = float('inf') # Set to infinite.
                min_position = None
                y1 = y + 1
                for column in [x - 1, x, x + 1]: # Check the lower three element and find min.
                    if column >= 0 and column < xtotal: # Inside boarder.
                        # e = None
                        if min_e_map[y1][column] != None:
                            e = min_e_map[y1][column] + Energy(y, x) # Cumulative energy.
                        else:
                            e = MinEnergyMap(y1, column) + Energy(y, x)
                        if e < minimum: # Update.
                            minimum = e
                            min_position = column
                min_e_map[y][x] = minimum # Cumulative minimum energy
                trace[y][x] = [y + 1, min_position] # [r,c] = [y,x]
                return min_e_map[y][x]

        # Build the table using bottom-up approach.
        for y in range(ytotal - 1, 0, -1): 
            for x in range(0, xtotal):
                MinEnergyMap(y, x)

        overall_min = float('inf') # Set to infinite.
        start = None
        for count in range(xtotal):
            weight = MinEnergyMap(0, count)
            if weight < overall_min:
                overall_min = weight
                start = [0, count] # [x,y]. Find the start.
        start_y = start[0]
        start_x = start[1]
        current_x = start_x
        current_y = start_y
        final_path = [start_x] # Final return, the seam.

        while trace[current_y][current_x] != None: # Go through the trace table.
            local = trace[current_y][current_x]
            final_path.append(local[1]) # Get the next pixel.
            current_y = local[0]
            current_x = local[1]

        self.seam = final_path

        return overall_min # From cumulative table.

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    #
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    #
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seam