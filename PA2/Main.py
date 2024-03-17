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
import sys
import time
from RobotMulcher import RobotMulcher

fp = open("test2.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())

# int_list = []
# for str in points:
#     str.split(" ")
#     print(str)
#     int_list.append(str)
# print(points)


# Call the compute function passing in the
# contents of the file
start = time.time()
rm = RobotMulcher()
print(rm.compute(points))
end = time.time()
print("time: "+ str(end-start))
