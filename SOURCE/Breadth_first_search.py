from Classes import Maze

def Breadth_first_search(graph: Maze, start, goal):
    # keep track of explored nodes
    expanded_list = []
    # keep track of all the paths to be checked
    path_list = [[start]]
 
    # return nothing if goal is start
    if start == goal:
        return [], []
 
    # test run all given paths until path_list is empty
    while path_list:
        # pop the oldest path from the path_list -> FIFO
        path = path_list.pop(0)
        # get the furthest node in path
        node = path[-1]
        if node not in expanded_list:
            # get node's adjacent_list
            neighbours = (graph.getNode(node)).adjacent_list()
            # if input data is wrong (no node exist at given location)
            if neighbours == None:
                break
            # check go through all neighbour nodes, create a new path and add it into the testing_paths
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                path_list.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    expanded_list.append(node)
                    return expanded_list, new_path 
 
            # mark node as explored
            expanded_list.append(node)
    # if no result can be found
    return None