from Classes import Maze
from operator import attrgetter

step_cost = 1

class Evaluation:
    def __init__(self, cost, node_path):
        self.cost = cost
        self.path = node_path
        
    def getCost(self):
        return self.cost
    
    def getPath(self):
        return self.path
        
        
    def getFurthestNode(self):
        if self.path:
            return int(self.path[-1])
        return None
    
    def __str__(self):
        return "C: " + str(self.cost) + "- P: " + str(self.path) 

def lastValue(path):
    return path[-1]

def ExploreFrontier(frontier_list):    
    if frontier_list:
        possible_path = []
        # a large random number is chosen for later comparison to get minimum value
        min = 99999*99999 
        
        for item in frontier_list:
            cur_cost = item.getCost()
            if cur_cost < min: # if a shorter cost is found, update possible_path and min value 
                min = cur_cost
                possible_path.clear()
                possible_path.append(item.getPath())
            elif cur_cost == min: # found another possible path with the same minimum cost
                possible_path.append(item.getPath())
    
        possible_path = sorted(possible_path, key = lastValue) # bring the path with smaller value name to the top
        
        best_path = possible_path[0]
        # frontier_list.remove((min, max_values[0]))
        frontier_list.pop(0) # pop the best result before returning it
        return Evaluation(min, best_path)
    
    return None


def is_in_frontier(node, frontier):
    for index in range(len(frontier)):
        item: Evaluation = frontier[index]
        path_item: list = item.getPath()
        if path_item[-1] == node:
            return index
    return None


def Uniform_cost_search(graph: Maze, start, goal):
    if goal == start:
        return [], []
    
    path_cost = 0
    path = []
    path.append(start)
    expanded = []    
    frontier = []
    frontier.append(Evaluation(path_cost, path))
    
    while 1:
        item = ExploreFrontier(frontier)
        if item is None:
            break
        
        current_node = item.getFurthestNode()
        current_path = (item.getPath()).copy()
        current_cost = item.getCost()
        # print(current_path)
        expanded.append(current_node)
        
        # if goal was in frontier
        if current_node == goal:
            return expanded, current_path     
        
        neighbours = (graph.getNode(current_node)).adjacent_list()
        '''
        for index in range(len(neighbours)):
            print(index, neighbours[index])
        '''    
        for neighbour in neighbours:
            new_path = current_path.copy()
            new_path.append(neighbour)
            new_cost = current_cost + step_cost
            new_item = Evaluation(new_cost, new_path)
        
            in_frontier = is_in_frontier(neighbour, frontier)
            if in_frontier is None:
                if neighbour not in expanded:
                    frontier.append(new_item)
            else:
                if frontier[in_frontier].getCost() > new_cost:
                    frontier.pop(in_frontier)
                    frontier.append(new_item)
    
    return None, None
    