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
# Your Computing ID: yl2nr
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import math
class SeamCarving:
    def __init__(self):
        self.seam = []
        self.num_rec = 0
        return
        

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def compute(self, image):
        nrows = len(image)
        ncols = len(image[0])
        #print(nrows,ncols)
        memo_energy = [[None for k in range(ncols)] for i in range(nrows)]
        memo_path = [[None for k in range(ncols)] for i in range(nrows)]

        def difference(a,b):
            reddiff = (a[0]-b[0])*(a[0]-b[0])
            greendiff = (a[1]-b[1])*(a[1]-b[1])
            bluediff = (a[2]-b[2])*(a[2]-b[2])
            diff = math.sqrt(reddiff+bluediff+greendiff)
            return diff
    
        def energy(r,c):
            num_of_neighbor = 0
            total_e = 0
            for i in [r-1,r,r+1]:
                for j in [c-1,c,c+1]:
                    if i == r and j == c:
                        continue
                    if i < 0 or i >= nrows:
                        continue
                    if j < 0 or j >= ncols:
                        continue
                    #print(i,j)
                    total_e += difference(image[r][c],image[i][j])
                    num_of_neighbor += 1
            local_energy = float(total_e/num_of_neighbor)
            return local_energy

        def minenergy (r,c):
            if r == nrows-1:
                memo_energy[r][c] = energy(r,c)
                return memo_energy[r][c]
            else: 
                min_e = 9999999.999
                min_col = None
                row = r+1
                #print (r,r-1)
                for col in [c-1,c,c+1]:
                    if col >= 0 and col < ncols:
                        current_e = None
                        if memo_energy[row][col] != None:
                            current_e = memo_energy[row][col] + energy(r,c)
                        else:
                            self.num_rec += 1
                            current_e = minenergy(row,col) + energy(r,c)
                        if current_e < min_e:
                            min_e = current_e
                            min_col = col
                    else:
                        continue
                memo_energy[r][c] = min_e
                memo_path[r][c] = [r+1,min_col]
                return memo_energy[r][c]

        # Bottom Up Iteration
        for it_r in range(nrows-1,0,-1):
            for it_c in range(0,ncols):
                minenergy(it_r,it_c)

        total_min = 9999999.9999
        start_point = None
        for str_col in range(ncols):
            weight = minenergy(0,str_col)
            if weight < total_min:
                total_min = weight
                start_point = [0,str_col]

        start_r = start_point[0]
        start_c = start_point[1]

        cur_r = start_r
        cur_c = start_c
        path = [start_c]

        while memo_path[cur_r][cur_c] != None:
            local_path = memo_path[cur_r][cur_c]
            path.append(local_path[1])
            cur_r = local_path[0]
            cur_c = local_path[1]

        self.seam = path

        return total_min

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seam