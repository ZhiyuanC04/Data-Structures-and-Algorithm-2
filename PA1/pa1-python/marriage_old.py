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
        # global lukePath, lorelaiPath
        # Create the graph (stored in dictionary)
        graph = {}
        node_count = 0
        vertexes = [item.strip() for item in file_data]
        vertexes0 = vertexes
        vertexes1 = vertexes[3:]
        for vertex in vertexes1:
            vertex = vertex.replace(' ', '')
            graph[str(node_count)] = []
            for node in vertex:
                graph[str(node_count)].append(node)
            node_count += 1
        # Set Luke and Lorelai's origin and destination
        Luke_start = vertexes0[1][0]
        Luke_end = vertexes0[1][2]
        Lorelai_start = vertexes0[2][0]
        Lorelai_end = vertexes0[2][2]
        #####
        # BFS Luke's path and BFS Lorelai's path that avoid collide Luke.
        Luke_Queue_1 = [[Luke_start]]
        Luke_Visited_1 = [Luke_start]
        Luke_ShortPath_1 = []
        while Luke_Queue_1: # BFS to find Luke's path
            Luke_CurrentPath_1 = Luke_Queue_1.pop(0)
            Luke_CurrentNode_1 = Luke_CurrentPath_1[-1]
            if Luke_CurrentNode_1 == Luke_end:
                Luke_ShortPath_1 = Luke_CurrentPath_1
                break
            for neighbor in graph[Luke_CurrentNode_1]:
                if neighbor not in Luke_Visited_1:
                    Luke_Visited_1.append(neighbor)
                    a = Luke_CurrentPath_1.copy()
                    a.append(neighbor)
                    Luke_Queue_1.append(a)
        #####
        # BFS Lorelai's path that don't collide Luke's path.
        Lorelai_Queue_1 = [[Lorelai_start]]
        Lorelai_Visited_1 = [Lorelai_start]
        Lorelai_ShortPath_1 = []
        Lorelai_TempMem = ""
        Lorelai_RepeatedCount = 0
        index_count_1 = 1
        while Lorelai_Queue_1:  # BFS to find Lorelai's path
            Lorelai_CurrentPath_1 = Lorelai_Queue_1.pop(0)
            Lorelai_CurrentNode_1 = Lorelai_CurrentPath_1[-1]
            if Lorelai_TempMem == Lorelai_CurrentNode_1:
                Lorelai_RepeatedCount += 1
            if Lorelai_RepeatedCount == 5:
                Lorelai_ShortPath_1 = []
                break
            Lorelai_TempMem = Lorelai_CurrentNode_1
            if Lorelai_CurrentNode_1 == Lorelai_end:
                Lorelai_ShortPath_1 = Lorelai_CurrentPath_1
                break
            for neighbor in graph[Lorelai_CurrentNode_1]:
                if neighbor not in Lorelai_Visited_1:
                    if neighbor == Luke_ShortPath_1[index_count_1]:
                        if Lorelai_CurrentNode_1 in Lorelai_Visited_1:
                            Lorelai_Visited_1.remove(Lorelai_CurrentNode_1)
                    # if neighbor not in Lorelai_Visited_1:
                    elif neighbor in graph[Luke_ShortPath_1[index_count_1]]:
                        if Lorelai_CurrentNode_1 in Lorelai_Visited_1:
                            Lorelai_Visited_1.remove(Lorelai_CurrentNode_1)
                    else:
                    # Not visited, new vertex and not collide with Luke. Go there.
                        Lorelai_Visited_1.append(neighbor)
                        b3 = Lorelai_CurrentPath_1.copy()
                        b3.append(neighbor)
                        Lorelai_Queue_1.append(b3)
            index_count_1 += 1
            if index_count_1 == len(Luke_ShortPath_1):
                Luke_ShortPath_1.append(Luke_ShortPath_1[-1])
        # print("BFS2 done")
        #####
        # BFS Lorelai's path and BFS Luke's path that avoid collide Luke.
        Lorelai_Queue_2 = [[Lorelai_start]]
        Lorelai_Visited_2 = [Lorelai_start]
        Lorelai_ShortPath_2 = []
        while Lorelai_Queue_2:  # BFS to find Lorelai's path
            Lorelai_CurrentPath_2 = Lorelai_Queue_2.pop(0)
            Lorelai_CurrentNode_2 = Lorelai_CurrentPath_2[-1]
            if Lorelai_CurrentNode_2 == Lorelai_end:
                Lorelai_ShortPath_2 = Lorelai_CurrentPath_2
                Lorelai_Queue_2 = []
                break
            for neighbor in graph[Lorelai_CurrentNode_2]:
                if neighbor not in Lorelai_Visited_2:
                    Lorelai_Visited_2.append(neighbor)
                    c = Lorelai_CurrentPath_2.copy()
                    c.append(neighbor)
                    Lorelai_Queue_2.append(c)
        #####
        # BFS Luke's path that don't collide Lorelai's path.
        Luke_Queue_2 = [[Luke_start]]
        Luke_Visited_2 = [Luke_start]
        Luke_ShortPath_2 = []
        Luke_TempMem = []
        Luke_RepeatedCount = 0
        index_count_2 = 1
        while Luke_Queue_2:  # BFS to find Luke's path
            Luke_CurrentPath_2 = Luke_Queue_2.pop(0)
            Luke_CurrentNode_2 = Luke_CurrentPath_2[-1]
            if Luke_TempMem == Luke_CurrentNode_2:
                Luke_RepeatedCount += 1
            if Luke_RepeatedCount == 5:
                Lorelai_ShortPath_1 = []
                break
            Luke_TempMem = Luke_CurrentNode_2
            if Luke_CurrentNode_2 == Luke_end:
                Luke_ShortPath_2 = Luke_CurrentPath_2
                break
            for neighbor in graph[Luke_CurrentNode_2]:
                if neighbor not in Luke_Visited_2:
                    if neighbor == Lorelai_ShortPath_2[index_count_2]:
                        if Luke_CurrentNode_2 in Luke_Visited_2:
                            Luke_Visited_2.remove(Luke_CurrentNode_2)
                    elif neighbor in graph[Lorelai_ShortPath_2[index_count_2]]:
                        if Luke_CurrentNode_2 in Luke_Visited_2:
                            Luke_Visited_2.remove(Luke_CurrentNode_2)
                    else:
                        # Not visited, new vertex and not collide with Lorelai. Go there.
                        Luke_Visited_2.append(neighbor)
                        c3 = Luke_CurrentPath_2.copy()
                        c3.append(neighbor)
                        Luke_Queue_2.append(c3)
            index_count_2 += 1
            if index_count_2 == len(Lorelai_ShortPath_2):
                Lorelai_ShortPath_2.append(Lorelai_ShortPath_2[-1])
        #####
        # Make the path same length:
        length_difference_1 = len(Luke_ShortPath_1) - len(Lorelai_ShortPath_1)
        if length_difference_1 > 0:
            Luke_ShortPath_1 = Luke_ShortPath_1[:-length_difference_1]
        length_difference_2 = len(Lorelai_ShortPath_2) - len(Luke_ShortPath_2)
        if length_difference_2 > 0:
            Lorelai_ShortPath_2 = Lorelai_ShortPath_2[:-length_difference_2]

        PathChoose = 1
        if (Luke_ShortPath_2 == []):
            PathChoose = 1
        elif (Lorelai_ShortPath_1 == []):
            PathChoose = 2
        elif (len(Luke_ShortPath_1) < len(Lorelai_ShortPath_2)):
            PathChoose = 1
        elif (len(Lorelai_ShortPath_2) < len(Luke_ShortPath_1)):
            PathChoose = 2
        #####
        result = 0
        if PathChoose == 1:
            for n1 in Luke_ShortPath_1:
                self.lukePath.append(int(n1))
            for n2 in Lorelai_ShortPath_1:
                self.lorelaiPath.append(int(n2))
            result = len(self.lukePath)
        elif PathChoose == 2:
            for n1 in Luke_ShortPath_2:
                self.lukePath.append(int(n1))
            for n2 in Lorelai_ShortPath_2:
                self.lorelaiPath.append(int(n2))
            result = len(self.lukePath)
        return result