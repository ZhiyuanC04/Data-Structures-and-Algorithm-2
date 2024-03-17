# CS3100 - Fall 2023 - Programming Assignment 1
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

class Marriage:
    lukePath = []
    lorelaiPath = []

    def __init__(self):
        return

    def getLukePath(self):
        return self.lukePath

    def getLorelaiPath(self):
        return self.lorelaiPath

    # This is the method that should set off the computation
    # of marriage.  It takes as input a list lines of input
    # as strings.  You should parse that input and then compute 
    # the shortest paths that both Luke and Lorelai should take.
    # The class fields of lukePath and lorelaiPath should be filled
    # with their respective paths.  The getters above will be called
    # by the grader script.
    #
    # @return the length of the shortest paths (in rooms)
    def compute(self, file_data):
        graph = {}
        # Create the graph (stored in dictionary)
        numberofvertex = int(file_data[0])
        # Set Luke and Lorelai's origin and destination
        Luke_start = int(file_data[1].split()[0])
        Luke_end = int(file_data[1].split()[1])
        Lorelai_start = int(file_data[2].split()[0])
        Lorelai_end = int(file_data[2].split()[1])
        # Create the key in dictionary based on number of vertex given
        for count in range(3,len(file_data)):
            neighbor = file_data[count].split()
            graph[count - 3] = []  # The value of the key is a list (of int)
            for vertex in neighbor:
                graph[count-3].append(int(vertex))
        #####1.1
        # BFS Luke's path and BFS Lorelai's path that avoid collide Luke.
        Luke_Visited_1 = [False] * numberofvertex
        # The index of the boolean value is corresponding to vertex
        Luke_Queue_1 = [[Luke_start]]
        # The queue that will pop and go through BFS
        Luke_Depth_1 = [-1] * numberofvertex
        # Record the sequence of vertex Luke go through.
        Luke_Visited_1[Luke_start] = True
        Luke_Depth_1[Luke_start] = 1
        Luke_ShortPath_1 = []
        # Final Path that is shortest for Luke.
        while Luke_Queue_1: # BFS to find Luke's path
            Luke_CurrentPath_1 = Luke_Queue_1.pop(0)
            Luke_CurrentNode_1 = Luke_CurrentPath_1[-1]
            if Luke_CurrentNode_1 == Luke_end:
                # Reaches the destination.
                Luke_ShortPath_1 = Luke_CurrentPath_1
                break
            for neighbor in graph[Luke_CurrentNode_1]:
                if Luke_Visited_1[neighbor] == False: # Not visited.
                    Luke_Visited_1[neighbor] = True # Visit it now.
                    Luke_Depth_1[neighbor] = Luke_Depth_1[Luke_CurrentNode_1] + 1
                    # It is the next stop after current room.
                    a = Luke_CurrentPath_1.copy()
                    a.append(neighbor)
                    Luke_Queue_1.append(a)
        Luke_FinalLen_1 = len(Luke_ShortPath_1)
        #####1.2
        # BFS Lorelai's path that don't collide Luke's path.
        Lorelai_Visited_1 = [False] * numberofvertex # Similar to above
        Lorelai_Queue_1 = [[Lorelai_start]]
        Lorelai_Depth_1 = [-1] * numberofvertex
        Lorelai_Visited_1[Lorelai_start] = True
        Lorelai_Depth_1[Lorelai_start] = 1
        Lorelai_ShortPath_1 = []
        Lorelai_TempMem = -1
        Lorelai_RepeatedCount = 0
        while Lorelai_Queue_1:  # BFS to find Lorelai's path
            Lorelai_CurrentPath_1 = Lorelai_Queue_1.pop(0)
            Lorelai_CurrentNode_1 = Lorelai_CurrentPath_1[-1]
            if Lorelai_CurrentNode_1 == Lorelai_end:
                Lorelai_ShortPath_1 = Lorelai_CurrentPath_1
                break
            for neighbor in graph[Lorelai_CurrentNode_1]:
                if Lorelai_Visited_1[neighbor] == False:
                    Lorelai_Depth_1[neighbor] = Lorelai_Depth_1[Lorelai_CurrentNode_1] + 1
                    Layer = Lorelai_Depth_1[neighbor]
                    if Layer - 1 < Luke_FinalLen_1:
                        Luke_ShortPath_1.append(Luke_ShortPath_1[-1])
                    if Luke_ShortPath_1[Lorelai_Depth_1[neighbor] - 1] in graph[neighbor]:
                        # Want to check if its neighbor is neighbor of Luke's current room.
                        # But it fail the test cases.
                        Lorelai_Visited_1[Lorelai_CurrentNode_1] = False
                        Lorelai_Depth_1[neighbor] = -1
                    elif Luke_ShortPath_1[Lorelai_Depth_1[neighbor] - 1] == neighbor:
                        # Delete current node from visited, meaning go backward and will come back.
                        Lorelai_Visited_1[Lorelai_CurrentNode_1] = False
                        Lorelai_Depth_1[neighbor] = -1
                    else:
                        # Not visited and will not collide Luke, so add it to the queue.
                        b = Lorelai_CurrentPath_1.copy()
                        b.append(neighbor)
                        Lorelai_Queue_1.append(b)
                        Lorelai_Visited_1[neighbor] = True
        #####2.1
        # BFS Lorelai's path and BFS Luke's path that avoid collide Luke.
        Lorelai_Visited_2 = [False] * numberofvertex # Similar as above.
        Lorelai_Queue_2 = [[Lorelai_start]]
        Lorelai_Depth_2 = [-1] * numberofvertex
        Lorelai_Visited_2[Lorelai_start] = True
        Lorelai_Depth_2[Lorelai_start] = 1
        Lorelai_ShortPath_2 = []
        while Lorelai_Queue_2:  # BFS to find Lorelai's path
            Lorelai_CurrentPath_2 = Lorelai_Queue_2.pop(0)
            Lorelai_CurrentNode_2 = Lorelai_CurrentPath_2[-1]
            if Lorelai_CurrentNode_2 == Lorelai_end:
                Lorelai_ShortPath_2 = Lorelai_CurrentPath_2
                break
            for neighbor in graph[Lorelai_CurrentNode_2]:
                if Lorelai_Visited_2[neighbor] == False:
                    Lorelai_Visited_2[neighbor] = True
                    Lorelai_Depth_2[neighbor] = Lorelai_Depth_2[Lorelai_CurrentNode_2] + 1
                    c = Lorelai_CurrentPath_2.copy()
                    c.append(neighbor)
                    Lorelai_Queue_2.append(c)
        Lorelai_FinalLen_2 = len(Lorelai_ShortPath_2)
        #####2.2
        # BFS Luke's path that don't collide Lorelai's path.
        Luke_Visited_2 = [False] * numberofvertex # Similar as above
        Luke_Queue_2 = [[Luke_start]]
        Luke_Depth_2 = [-1] * numberofvertex
        Luke_Visited_2[Luke_start] = True
        Luke_Depth_2[Luke_start] = 1
        Luke_ShortPath_2 = []
        Luke_TempMem = -1
        Luke_RepeatedCount = 0
        while Luke_Queue_2:
            Luke_CurrentPath_2 = Luke_Queue_2.pop(0)
            Luke_CurrentNode_2 = Luke_CurrentPath_2[-1]
            if Luke_CurrentNode_2 == Luke_end:
                Luke_ShortPath_2 = Luke_CurrentPath_2
                break
            for neighbor in graph[Luke_CurrentNode_2]:
                if Luke_Visited_2[neighbor] == False:
                    Luke_Depth_2[neighbor] = Luke_Depth_2[Luke_CurrentNode_2] + 1
                    Layer = Luke_Depth_2[neighbor]
                    if Layer - 1 < Lorelai_FinalLen_2:
                        Lorelai_ShortPath_2.append(Lorelai_ShortPath_2[-1])
                    if Lorelai_ShortPath_2[Luke_Depth_2[neighbor] - 1] in graph[neighbor]:
                        # Luke_Depth_2[Luke_CurrentNode_2] += 1
                        # Luke_Depth_2[neighbor] = -1
                        # d = Luke_CurrentPath_2.copy()
                        # d.append(Luke_CurrentNode_2)
                        # Luke_Queue_2.append(d)
                        Luke_Visited_2[Luke_CurrentNode_2] = False
                        Luke_Depth_2[neighbor] = -1
                    elif Lorelai_ShortPath_2[Luke_Depth_2[neighbor] - 1] == neighbor:
                        Luke_Visited_2[Luke_CurrentNode_2] = False
                        Luke_Depth_2[neighbor] = -1
                    else:
                        d = Luke_CurrentPath_2.copy()
                        d.append(neighbor)
                        Luke_Queue_2.append(d)
                        Luke_Visited_2[neighbor] = True
        #####3
        # Third way, run the BFS at same time and let each other avoid them.
# Luke_start, Luke_end = map(int, file_data[1].split())
# Lorelai_start, Lorelai_end = map(int, file_data[2].split())
        AdjacentGraph = [list(map(int, line.split())) for line in file_data[3:]]
        # Use Map to change all value to integer.
        # Create a list that the index is the vertex name, and the value is the neighbor
        Visited = []
        # Use a list to record what vertex is visited
        Queue = [(Luke_start, Lorelai_start, 0)]
        ParentVertex = {(Luke_start, Lorelai_start): None}
        result = 0
        Luke_Path_3 = []
        Lorelai_Path_3 = []
        while Queue:
            Luke, Lorelai, Position = Queue.pop(0)
            if Luke == Luke_end and Lorelai == Lorelai_end:
                Luke_Final = []
                Lorelai_Final = []
                while (Luke, Lorelai) != (Luke_start, Lorelai_start):
                    Luke_Final.append(Luke)
                    Lorelai_Final.append(Lorelai)
                    Luke, Lorelai = ParentVertex[(Luke, Lorelai)]
                self.lukePath = [Luke_start] + Luke_Final[::-1]
                self.lorelaiPath = [Lorelai_start] + Lorelai_Final[::-1]
                result = Position + 1
            for Next_Luke in AdjacentGraph[Luke] + [Luke]:
                for Next_Lorelai in AdjacentGraph[Lorelai] + [Lorelai]:
                    if Next_Luke != Next_Lorelai:
                        if Next_Luke not in AdjacentGraph[Next_Lorelai]:
                            if Next_Lorelai not in AdjacentGraph[Next_Luke]:
                                if (Next_Luke, Next_Lorelai) not in Visited:
                                    Visited.append((Next_Luke, Next_Lorelai))
                                    Queue.append((Next_Luke, Next_Lorelai, Position + 1))
                                    ParentVertex[(Next_Luke, Next_Lorelai)] = (Luke, Lorelai)
        #####
        # Make the path same length:
        PathChoose = 3
        if (Luke_ShortPath_2 == []):
            # If ShortPath2 is [], meaning its queue is empty and there is no path avaliable.
            # Use ShortPaath1
            PathChoose = 3
        elif (Lorelai_ShortPath_1 == []):
            PathChoose = 3
        else:
            if (len(Lorelai_ShortPath_1) < len(Luke_ShortPath_2)):
                PathChoose = 1
            elif (len(Luke_ShortPath_2) < len(Lorelai_ShortPath_1)):
                PathChoose = 2
        #####
        if PathChoose == 1:
            length_difference_1 = len(Luke_ShortPath_1) - len(Lorelai_ShortPath_1)
            if length_difference_1 > 0:
                Luke_ShortPath_1 = Luke_ShortPath_1[:-length_difference_1]
            if len(Luke_ShortPath_1) < len(Luke_Path_3):
                self.lukePath = Luke_ShortPath_1
                self.lorelaiPath = Lorelai_ShortPath_1
                result = len(self.lorelaiPath)
            else:
                self.lukePath = Luke_Path_3
                self.lorelaiPath = Lorelai_Path_3
        elif PathChoose == 2:
            length_difference_2 = len(Lorelai_ShortPath_2) - len(Luke_ShortPath_2)
            if length_difference_2 > 0:
                Lorelai_ShortPath_2 = Lorelai_ShortPath_2[:-length_difference_2]
            if len(Lorelai_ShortPath_2) < len(Lorelai_Path_3):
                self.lukePath = Luke_ShortPath_2
                self.lorelaiPath = Lorelai_ShortPath_2
                result = len(self.lukePath)
            else:
                self.lukePath = Luke_Path_3
                self.lorelaiPath = Lorelai_Path_3
        return result