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
        luke_start, luke_end = map(int, file_data[1].split())
        lorelai_start, lorelai_end = map(int, file_data[2].split())
        adj = [list(map(int, line.split())) for line in file_data[3:]]
        visited = set()
        q = [(luke_start, lorelai_start, 0)]
        parent = {(luke_start, lorelai_start): None}
        while q:
            u, v, t = q.pop(0)
            # If we reached the destination
            if u == luke_end and v == lorelai_end:
                luke_temp, lorelai_temp = [], []
                while (u, v) != (luke_start, lorelai_start):
                    luke_temp.append(u)
                    lorelai_temp.append(v)
                    u, v = parent[(u, v)]
                self.lukePath = [luke_start] + luke_temp[::-1]
                self.lorelaiPath = [lorelai_start] + lorelai_temp[::-1]
                return t

            # Luke's possible moves
            for next_u in adj[u] + [u]:
                # Lorelai's possible moves
                for next_v in adj[v] + [v]:
                    # Check if next move is valid
                    if next_u != next_v and \
                            next_u not in adj[next_v] and \
                            next_v not in adj[next_u] and \
                            (next_u, next_v) not in visited:
                        visited.add((next_u, next_v))
                        q.append((next_u, next_v, t + 1))
                        parent[(next_u, next_v)] = (u, v)
        return -1  # In case no valid path is found

        luke_start = int(file_data[1].split()[0])
        luke_end = int(file_data[1].split()[1])
        lorelai_start = int(file_data[2].split()[0])
        lorelai_end = int(file_data[2].split()[1])
        # luke_start, luke_end = map(int, file_data[1].split())
        # lorelai_start, lorelai_end = map(int, file_data[2].split())
        adj = [list(map(int, line.split())) for line in file_data[3:]]
        visited = set()
        q = [(luke_start, lorelai_start, 0)]
        parent = {(luke_start, lorelai_start): None}
        while q:
            a = q.pop(0)
            u = a[0]
            v = a[1]
            t = a[2]
            # If we reached the destination
            if u == luke_end and v == lorelai_end:
                luke_temp = []
                lorelai_temp = []
                while (u, v) != (luke_start, lorelai_start):
                    luke_temp.append(u)
                    lorelai_temp.append(v)
                    u, v = parent[(u, v)]
                self.lukePath = [luke_start] + luke_temp[::-1]
                self.lorelaiPath = [lorelai_start] + lorelai_temp[::-1]
                return t + 1

            # Luke's possible moves
            for next_u in adj[u] + [u]:
                # Lorelai's possible moves
                for next_v in adj[v] + [v]:
                    # Check if next move is valid
                    if next_u != next_v:
                        if next_u not in adj[next_v]:
                            if next_v not in adj[next_u]:
                                if (next_u, next_v) not in visited:
                                    visited.add((next_u, next_v))
                                    q.append((next_u, next_v, t + 1))
                                    parent[(next_u, next_v)] = (u, v)
        return -1  # In case no valid path is found

pair_srt = (start_lk,start_lr)
        visited_both = []
        visited_both.append(pair_srt)
        lkp = []
        lrp = []
        path_both =[[(start_lk, start_lr)]]
        time=0
        while path_both:
            path = path_both.pop(0)
            current_lk = path[-1][0]
            current_lr = path[-1][1]
            if current_lk == end_lk and current_lr == end_lr:
                for i in path:
                    time += 1
                    lkp.append(i[0])
                    lrp.append(i[1]) # 如果一个先到终点
            elif current_lk == end_lk:
                for r in graph[current_lr] + [current_lr]:
                    if current_lk != r and current_lk not in graph[r] and r not in graph[current_lk]:
                        if (current_lk, r) not in visited_both:
                            visited_both.append((current_lk,r))
                            new_path = list(path)
                            new_path.append((current_lk,r))
                            path_both.append(new_path)
            elif current_lr == end_lr:
                for k in graph[current_lk] + [current_lk]:
                    if k != current_lr and k not in graph[r] and current_lr not in graph[k]:
                        if (k, current_lr) not in visited_both:
                            visited_both.append((k,current_lr))
                            new_path = list(path)
                            new_path.append((k,current_lr))
                            path_both.append(new_path)
            else:
                for k in graph[current_lk] + [current_lk]:
                    for r in graph[current_lr] + [current_lr]:
                        if k != r and k not in graph[r] and r not in graph[k]:
                            if (k, r) not in visited_both:
                                visited_both.append((k,r))
                                new_path = list(path)
                                new_path.append((k,r))
                                path_both.append(new_path)

