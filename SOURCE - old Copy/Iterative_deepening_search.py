from Classes import Maze, Node

max_depth = 7
def recursive_depth_limited_search(graph: Maze, current_node: int, goal, limit):
    if(goal == None):
        return True, Node
    
    return None

    # If reached the depth limit, stop recursing. 
    if limit <= 0 : 
        return False, None
    
    
    node = graph.getNode(current_node)
    nearby_nodes = node.adjacent_list()
    path = []
    path.append(current_node)
    # Recur for all the vertices adjacent to this vertex 
    for item in nearby_nodes:
        res, _path = recursive_depth_limited_search(graph, item, goal, limit - 1)
        if(res): 
            return True, path.append(path)
        
    return False, None
  
# IDDFS to search if target is reachable from v. 
# It uses recursive DLS() 
def Iterative_deepening_search(graph: Maze, start, goal): 
    
    # Repeatedly depth-limit search till the maximum depth 
    for lim in range(max_depth): 
        if (recursive_depth_limited_search(graph, start, goal, lim)): 
            break
    return None
