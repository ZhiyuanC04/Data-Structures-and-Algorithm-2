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
# Your Computing ID: yl2nr
# Collaborators: 
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
        num_ver = int(file_data[0])
        for i in range(int(file_data[0])):
            graph[int(i)] = []
        start_lk = int(file_data[1].split()[0])
        end_lk = int(file_data[1].split()[1])
        start_lr = int(file_data[2].split()[0])
        end_lr = int(file_data[2].split()[1])

        for k in range(3,len(file_data)):
            neighbor = file_data[k].split()
            for n in neighbor:
                graph[k-3].append(int(n))
        
        visited_lk = [False]*num_ver
        visited_lr = [False]*num_ver
        path_lk = []
        path_lr = []
        depth_lk = [-1]*num_ver
        depth_lr = [-1]*num_ver

        path_lk.append([start_lk])
        path_lr.append([start_lr])
        visited_lk[start_lk] = True
        visited_lr[start_lr] = True
        depth_lk[start_lk] = 1
        depth_lr[start_lr] = 1

        final_path_lk = []
        final_path_lr = []
        def is_neighbor_lr(x):
            for n in graph[x]:
                if depth_lr[x] == depth_lk[n]:
                    return True
            return False

        while path_lk:
            current_path_lk = path_lk.pop(0)
            current_lk = current_path_lk[-1]
            if current_lk == end_lk:
                final_path_lk = current_path_lk
                break
            for m in graph[current_lk]:
                if visited_lk[m] == False:
                    depth_lk[m] = depth_lk[current_lk]+1
                    new_path_lk = list(current_path_lk)
                    new_path_lk.append(m)
                    path_lk.append(new_path_lk)
                    visited_lk[m] = True
        len_finallk = len(final_path_lk)
        while path_lr:
            current_path_lr = path_lr.pop(0)
            current_lr = current_path_lr[-1]
            if current_lr == end_lr:
                final_path_lr = current_path_lr
                break
            for j in graph[current_lr]:
                if visited_lr[j] == False:
                    depth_lr[j] = depth_lr[current_lr]+1
                    layer = depth_lr[j]
                    if layer-1 < len_finallk:
                        if final_path_lk[depth_lr[j]-1] == j or final_path_lk[depth_lr[j]-1] in graph[j]:
                            visited_lr[current_lr] = False
                            depth_lr[j] = -1
                        else:
                            new_path_lr = list(current_path_lr)
                            new_path_lr.append(j)
                            path_lr.append(new_path_lr)
                            visited_lr[j] = True
                    else:
                        new_path_lr = list(current_path_lr)
                        new_path_lr.append(j)
                        path_lr.append(new_path_lr)
                        visited_lr[j] = True
            
        #print(final_path_lk,final_path_lr)

        final_path_lk2 = []
        final_path_lr2 = []
        visited_lk = [False]*num_ver
        visited_lr = [False]*num_ver
        path_lk = []
        path_lr = []
        depth_lk = [-1]*num_ver
        depth_lr = [-1]*num_ver

        path_lk.append([start_lk])
        path_lr.append([start_lr])
        visited_lk[start_lk] = True
        visited_lr[start_lr] = True
        depth_lk[start_lk] = 1
        depth_lr[start_lr] = 1

        while path_lr:
            current_path_lr = path_lr.pop(0)
            current_lr = current_path_lr[-1]
            if current_lr == end_lr:
                final_path_lr2 = current_path_lr
                break
            for j in graph[current_lr]:
                if visited_lr[j] == False:
                    depth_lr[j] = depth_lr[current_lr]+1
                    new_path_lr = list(current_path_lr)
                    new_path_lr.append(j)
                    path_lr.append(new_path_lr)
                    visited_lr[j] = True
        len_finallr = len(final_path_lr2)
        while path_lk:
            current_path_lk = path_lk.pop(0)
            current_lk = current_path_lk[-1]
            if current_lk == end_lk:
                final_path_lk2 = current_path_lk
                break
            for m in graph[current_lk]:
                if visited_lk[m] == False:
                    depth_lk[m] = depth_lk[current_lk]+1
                    layer = depth_lk[m]
                    if layer-1 < len_finallr:
                        if final_path_lr2[depth_lk[m]-1] == m or final_path_lr2[depth_lk[m]-1] in graph[m]:
                            visited_lk[current_lk] = False
                            depth_lk[m] = -1
                        else:
                            new_path_lk = list(current_path_lk)
                            new_path_lk.append(m)
                            path_lk.append(new_path_lk)
                            visited_lk[m] = True
                    else:
                        new_path_lk = list(current_path_lk)
                        new_path_lk.append(m)
                        path_lk.append(new_path_lk)
                        visited_lk[m] = True
        #print(final_path_lk2,final_path_lr2)
            #if path_lk == []:
                #if not (final_path_lr2[depth_lk[j]-1] == current_lk or final_path_lr2[depth_lk[m]-1] in graph[m]):
                    #path_lk.append([current_path_lk.append()])
        if final_path_lk2 == []:
            len_lk = len(final_path_lk)
            len_lr = len(final_path_lr)
            result = max(len_lk,len_lr)
            if len_lk <result:
                for i in range(len_lk,result):
                    final_path_lk.append(end_lk)
        
            if len_lr <result:
                for i in range(len_lr,result):
                    final_path_lr.append(end_lr)

            self.lorelaiPath = final_path_lr
            self.lukePath = final_path_lk
            return result

        elif final_path_lr == []:
            len_lk = len(final_path_lk2)
            len_lr = len(final_path_lr2)
            result = max(len_lk,len_lr)
            if len_lk <result:
                for i in range(len_lk,result):
                    final_path_lk2.append(end_lk)
        
            if len_lr <result:
                for i in range(len_lr,result):
                    final_path_lr2.append(end_lr)
            
            self.lorelaiPath = final_path_lr2
            self.lukePath = final_path_lk2
            return result
        else:
            len_lk2 = len(final_path_lk2)
            len_lr2 = len(final_path_lr2)
            len_lk = len(final_path_lk)
            len_lr = len(final_path_lr)
            if max(len_lk,len_lr) <= max(len_lk2,len_lr2):
                result = max(len_lk,len_lr)
                if len_lk <result:
                    for i in range(len_lk,result):
                        final_path_lk.append(end_lk)
        
                if len_lr <result:
                    for i in range(len_lr,result):
                        final_path_lr.append(end_lr)
                
                self.lorelaiPath = final_path_lr
                self.lukePath = final_path_lk
                return result
            else:
                result = max(len_lk2,len_lr2)
                if len_lk2 <result:
                    for i in range(len_lk2,result):
                        final_path_lk2.append(end_lk)
        
                if len_lr2 <result:
                    for i in range(len_lr2,result):
                        final_path_lr2.append(end_lr)
                self.lorelaiPath = final_path_lr2
                self.lukePath = final_path_lk2
                return result