# CS3100 - Fall 2023 - Programming Assignment 2
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
# Your Computing ID: Zhiyuan Chang(vgs3qt)
# Collaborators: Yining Liu(yl2nr), Yuhao Niu(bhb9ba)
# Sources: Introduction to Algorithms, Cormen
#################################
import math

class RobotMulcher:
    def __init__(self):
        # self.x = x
        # self.y = y
        return
    # This is the method that should set off the computation
    # of closest tree.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest distance
    # and return that value from this method
    # @return the distance between the closest trees
    def compute(self, file_data):
        int_list = self.sort_by_x(file_data)
        # print(int_list)
        find_min = self.eachsideclosest(int_list, len(int_list))
        return find_min

    def sort_by_x(self, file):
        # Make the list of string into a list of list of int.
        int_list  = [[float(num) for num in item.split()] for item in file]
        # Sort the list based on x value.
        int_list.sort(key = lambda x: x[0])
        # print(int_list)
        return int_list

    def eachsideclosest(self, file, length):
        # If there are only three points or less, then we just calculate it.
        if length <= 3:
            return self.calculation(file, length)
        # Use divide and conquer to get the cloest distance on eachside.
        mid = length // 2
        midPoint = file[mid]
        dleft = self.eachsideclosest(file[:mid], mid)
        dright = self.eachsideclosest(file[mid:], length - mid)
        if dleft < dright:
            d = dleft
        else:
            d = dright
        # print(d)
        # Calculate the middle part (check distance between points on right and left side).
        middle_part = []
        for i in range(length):
            if abs(file[i][0] - midPoint[0]) < d:
                middle_part.append(file[i])
        middle = self.middlepart_closest(middle_part, len(middle_part), d)
        # print(middle)
        if d < middle:
            return d
        else:
            return middle

    def calculation(self, file, length):
        # Calculate the distance betwee points
        min_distance = float("inf")
        for i in range(length):
            for j in range(i + 1, length):
                distance = math.sqrt((file[i][0] - file[j][0]) * (file[i][0] - file[j][0])
                                     + (file[i][1] - file[j][1]) * (file[i][1] - file[j][1]))
                if distance < min_distance:
                    min_distance = distance
        return min_distance

    def middlepart_closest(self, middle, length, sidesmall):
        min_dist = sidesmall
        # Sort based on y value.
        middle.sort(key = lambda x: x[1])
        # Compare the distance.
        for i in range(length):
            for j in range(i + 1, length):
                if (middle[j][1] - middle[i][1]) >= min_dist:
                    break
                distance = math.sqrt((middle[i][0] - middle[j][0]) * (middle[i][0] - middle[j][0])
                                     + (middle[i][1] - middle[j][1]) * (middle[i][1] - middle[j][1]))
                if distance < min_dist:
                    min_dist = distance
        return min_dist