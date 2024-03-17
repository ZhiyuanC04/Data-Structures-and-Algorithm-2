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
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import math

class SeamCarving:
    def __init__(self):
        self.trace = []
        self.index = 0
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def compute(self, image):
        map = self.Map(image)

        ytotal = len(map)
        xtotal = len(map[0])
        cumulative = []
        for a in range(ytotal):
            cumulative.append([])
            self.trace.append([])

        for all in map[xtotal-1]:
            cumulative[ytotal - 1].append(all)
            self.trace[ytotal - 1].append(-1)
        # print(cumulative)
        for i in range(ytotal - 2, -1, -1):
            for j in range(0, xtotal):
                if j == 0:
                    mid = map[i + 1][j]
                    right = map[i + 1][j + 1]
                    if right > mid:
                        choose = mid
                        choice = 1
                    else:
                        choose = right
                        choice = 2
                if j == xtotal - 1:
                    left = map[i + 1][j - 1]
                    mid = map[i + 1][j]
                    if mid > left:
                        choose = left
                        choice = 0
                    else:
                        choose = mid
                        choice = 1
                else:
                    left = map[i + 1][j - 1]
                    mid = map[i + 1][j]
                    right = map[i + 1][j + 1]
                    choose = min(left, mid, right)
                    if choose == left:
                        choice = 0
                    if choose == mid:
                        choice = 1
                    if choose == right:
                        choice = 2
                cumulative[i].append(map[i][j] + choose)
                if choose == 0:
                    self.trace[i].append(j - 1)
                elif choose == 2:
                    self.trace[i].append(j + 1)
                else:
                    self.trace[i].append(j)

        # print(cumulative)
        # print(self.trace)
        result = float('inf')
        for all in cumulative[0]:
            if all < result:
                result = all
        for i in range(0, xtotal):
            if result == cumulative[0][i]:
                self.index = i
                break
        return result

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        seam = [self.index]
        current = self.index
        keep_going = True
        # print(self.index)
        while keep_going:
            for y in range(0,len(self.trace)):
                if self.trace[y][current] == -1:
                    keep_going = False
                    break
                seam.append(self.trace[y][current])
                current = self.trace[y][current]
        return seam

    def Map(self, image):
        ytotal = len(image)
        xtotal = len(image[0])
        count = 0
        resultMap = []
        for i in range(ytotal):
            resultMap.append([])
        for ycor in range(ytotal):
            for xcor in range(xtotal):
                energy = 0.0
                if xcor - 1 >= 0: # Not most left column.
                    energy += self.calEnergy(image[xcor][ycor], image[xcor - 1][ycor])
                    count += 1
                    if ycor - 1 >= 0:
                        energy += self.calEnergy(image[xcor][ycor], image[xcor - 1][ycor - 1])
                        count += 1
                    if ycor + 1 < ytotal:
                        energy += self.calEnergy(image[xcor][ycor], image[xcor - 1][ycor + 1])
                        count += 1
                if ycor - 1 >= 0: # Not bottom row.
                    energy += self.calEnergy(image[xcor][ycor], image[xcor][ycor - 1])
                    count += 1
                if ycor + 1 < ytotal: # Not top row.
                    energy += self.calEnergy(image[xcor][ycor], image[xcor][ycor + 1])
                    count += 1
                if xcor + 1 < xtotal: # Not most right column.
                    energy += self.calEnergy(image[xcor][ycor], image[xcor + 1][ycor])
                    count += 1
                    if ycor - 1 >= 0:
                        energy += self.calEnergy(image[xcor][ycor], image[xcor + 1][ycor - 1])
                        count += 1
                    if ycor + 1 < ytotal:
                        energy += self.calEnergy(image[xcor][ycor], image[xcor + 1][ycor + 1])
                        count += 1
                energy = energy / count
                # print(energy)
                # print(count)
                resultMap[ycor].append(energy)
                count = 0
        # print(resultMap)
        return resultMap
    def calEnergy(self, ori, adj):
        energy = math.sqrt((adj[0] - ori[0])**2 + (adj[1] - ori[1])**2 + (adj[2] - ori[2])**2)
        # print(energy)
        return energy