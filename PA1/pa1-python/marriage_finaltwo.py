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

        start_lk = int(file_data[1].split()[0])
        end_lk = int(file_data[1].split()[1])
        start_lr = int(file_data[2].split()[0])
        end_lr = int(file_data[2].split()[1])

        graph = [list(map(int, line.split())) for line in file_data[3:]]
        prior = {(start_lk,start_lr): None}
        visited_both = set((start_lk, start_lr))
        path_both = [(start_lk, start_lr)]
        while path_both:
            path = path_both.pop(0)
            current_lk = path[0]
            current_lr = path[1]
            if current_lk == end_lk and current_lr == end_lr:
                lkp = []
                lrp = []
                while (current_lk, current_lr) != (start_lk, start_lr):
                    lkp.append(current_lk)
                    lrp.append(current_lr)
                    current_lk, current_lr = prior[(current_lk,current_lr)]
                lkp.append(current_lk)
                lrp.append(current_lr)
                self.lukePath = lkp[::-1]
                self.lorelaiPath = lrp[::-1]
                result = len(self.lukePath)
                break
            # elif current_lk == end_lk:
            #     for r in graph[current_lr] + [current_lr]:
            #             if current_lk != r and current_lk not in graph[r] and r not in graph[current_lk]:
            #                 if (current_lk, r) not in visited_both:
            #                     visited_both.add((current_lk, r))
            #                     path_both.append((current_lk, r))
            #                     prior[(current_lk, r)] = (current_lk, current_lr)
            #
            # elif current_lr == end_lr:
            #     for k in graph[current_lk] + [current_lk]:
            #         if k != current_lr and k not in graph[r] and current_lr not in graph[k]:
            #             if (k, current_lr) not in visited_both:
            #                 visited_both.add((k, current_lr))
            #                 path_both.append((k, current_lr))
            #                 prior[(k, current_lr)] = (current_lk, current_lr)
            else:
                for k in graph[current_lk] + [current_lk]:
                    for r in graph[current_lr] + [current_lr]:
                        if k != r and k not in graph[r] and r not in graph[k] and (k, r) not in visited_both:
                                visited_both.add((k, r))
                                path_both.append((k, r))
                                prior[(k, r)] = (current_lk, current_lr)
        return result

        # start_lk = int(file_data[1].split()[0])
        # end_lk = int(file_data[1].split()[1])
        # start_lr = int(file_data[2].split()[0])
        # end_lr = int(file_data[2].split()[1])
        # graph = [list(map(int, line.split())) for line in file_data[3:]]
        #
        # visited_both = set((start_lk, start_lr))
        # lkp = []
        # lrp = []
        # path_both = [[(start_lk, start_lr)]]
        # time = 0
        # while path_both:
        #     path = path_both.pop(0)
        #     current_lk = path[-1][0]
        #     current_lr = path[-1][1]
        #     if current_lk == end_lk and current_lr == end_lr:
        #         for i in path:
        #             time += 1
        #             lkp.append(i[0])
        #             lrp.append(i[1])
        #         break
        #     elif current_lk == end_lk:
        #         for k in [current_lk]:
        #             for r in graph[current_lr] + [current_lr]:
        #                 if k != r and k not in graph[r] and r not in graph[k]:
        #                     if (k, r) not in visited_both:
        #                         visited_both.add((k, r))
        #                         new_path = list(path)
        #                         new_path.append((k, r))
        #                         path_both.append(new_path)
        #     elif current_lr == end_lr:
        #         for r in [current_lr]:
        #             for k in graph[current_lk] + [current_lk]:
        #                 if k != r and k not in graph[r] and r not in graph[k]:
        #                     if (k, r) not in visited_both:
        #                         visited_both.add((k, r))
        #                         new_path = list(path)
        #                         new_path.append((k, r))
        #                         path_both.append(new_path)
        #     else:
        #         for k in graph[current_lk] + [current_lk]:
        #             for r in graph[current_lr] + [current_lr]:
        #                 if k != r and k not in graph[r] and r not in graph[k]:
        #                     if (k, r) not in visited_both:
        #                         visited_both.add((k, r))
        #                         new_path = list(path)
        #                         new_path.append((k, r))
        #                         path_both.append(new_path)
        # self.lukePath = lkp
        # self.lorelaiPath = lrp
        # result = len(self.lukePath)
        # return result
