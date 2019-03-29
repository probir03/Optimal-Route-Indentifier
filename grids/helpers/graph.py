from collections import defaultdict


class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {}
        self.optimized_time = 0

    def add_edge(self, start, end, distance, speed):
        '''Method to add an edge to the graph'''
        self.graph[start].append((end, distance, speed))
        self.graph[end].append((start, distance, speed))
        self.graph[start] = list(set(self.graph[start]))
        self.graph[end] = list(set(self.graph[end]))

    def get_graph(self):
        return self.graph

    def generate_edges(self):
        '''Method to generate edges of graph

        Args: None

        Return :
            List of tuples
        '''
        edges = []

        # for each node in graph
        for node in self.graph:

            # for each neighbour node of a single node
            for neighbour in self.graph[node]:

                # if edge exists then append
                edges.append((node, neighbour[0], neighbour[1] / neighbour[2]))
        return list(set(edges))

    def check_all_conected_nodes(self):
        '''Method to check all the nodes are connected or not
        '''
        total_comp = 0
        for item in self.graph:
            self.visited[item] = False
        for item in self.visited:
            if self.visited[item] == False:
                self.dfs(item)
                total_comp = total_comp + 1
        if total_comp > 1:
            return False
        return True

    def dfs(self, item):
        '''DFS method'''
        self.visited[item] = True
        for val in self.graph[item]:
            if self.visited[val[0]] == False:
                self.dfs(val[0])

    def find_all_path(self, start, end, path=[]):
        '''Method to find all the possible path'''
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.graph[start]:
            if node[0] not in path:
                newpaths = self.find_all_path(node[0], end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_optimal_path(self, start, end):
        '''Method to find optimal path'''
        paths = self.find_all_path(start, end)
        minimal_travel_time = 0
        optimal_path = None
        for path in paths:
            temp = 0
            for i in range(len(path) - 1):
                for item in self.graph[path[i]]:
                    if item[0] == path[i + 1]:
                        temp += item[1] / item[2]
            if(minimal_travel_time > temp or minimal_travel_time == 0):
                minimal_travel_time = temp
                optimal_path = path
        return optimal_path


