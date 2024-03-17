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

    def compute(self, file_data):
        start_lk = int(file_data[1].split()[0])
        end_lk = int(file_data[1].split()[1])
        start_lr = int(file_data[2].split()[0])
        end_lr = int(file_data[2].split()[1])
        graph = [list(map(int, line.split())) for line in file_data[3:]]
        pair_srt = (start_lk, start_lr)
        visited_both = []
        visited_both.append(pair_srt)
        lkp = []
        lrp = []
        path_both = [[(start_lk, start_lr)]]
        time = 0
        while path_both:
            path = path_both.pop(0)
            current_lk = path[-1][0]
            current_lr = path[-1][1]
            if current_lk == end_lk and current_lr == end_lr:
                for i in path:
                    time += 1
                    lkp.append(i[0])
                    lrp.append(i[1])
            # elif current_lk == end_lk:
            #     for r in graph[current_lr] + [current_lr]:
            #         if current_lk != r and current_lk not in graph[r] and r not in graph[current_lk]:
            #             if (current_lk, r) not in visited_both:
            #                 visited_both.append((current_lk, r))
            #                 new_path = list(path)
            #                 new_path.append((current_lk, r))
            #                 path_both.append(new_path)
            # elif current_lr == end_lr:
            #     for k in graph[current_lk] + [current_lk]:
            #         if k != current_lr and k not in graph[r] and current_lr not in graph[k]:
            #             if (k, current_lr) not in visited_both:
            #                 visited_both.append((k, current_lr))
            #                 new_path = list(path)
            #                 new_path.append((k, current_lr))
            #                 path_both.append(new_path)
            else:
                for k in graph[current_lk] + [current_lk]:
                    for r in graph[current_lr] + [current_lr]:
                        if k != r and k not in graph[r] and r not in graph[k]:
                            if (k, r) not in visited_both:
                                visited_both.append((k, r))
                                new_path = list(path)
                                new_path.append((k, r))
                                path_both.append(new_path)
        self.lukePath = lkp
        self.lorelaiPath = lrp
        result = len(self.lukePath)
        return result