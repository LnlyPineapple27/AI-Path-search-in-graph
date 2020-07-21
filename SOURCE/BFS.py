from Classes import Maze

def BFS_Search(graph: Maze, start, goal):
    # keep track of explored nodes
    expanded_list = []
    # keep track of all the paths to be checked
    testing_paths = [[start]]
 
    # return nothing if goal is start
    if start == goal:
        return [], []
 
    # test run all given paths until testing_paths is empty
    while testing_paths:
        # pop the oldest path from the testing_paths -> FIFO
        path = testing_paths.pop(0)
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
                testing_paths.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    expanded_list.append(node)
                    return expanded_list, new_path 
 
            # mark node as explored
            expanded_list.append(node)
    # if no result can be found
    return None