from Classes import Maze, Node

max_depth = 7
def recursive_depth_limited_search(graph: Maze, current_node: int, goal, limit, expanded):
    if(current_node == goal):
        return True, [current_node]

    # If reached the depth limit, stop recursing. 
    if limit <= 0 : 
        return False, []
    
    node: Node = graph.getNode(current_node)
    nearby_nodes = node.adjacent_list()
    path = [current_node]
    # Recur for all the vertices adjacent to this vertex 
    for item in nearby_nodes:
        res, child_path = recursive_depth_limited_search(graph, item, goal, limit - 1, expanded)
        expanded.append(item)
        if(res): 
            return True, path + child_path
        
    return False, []
  
def Iterative_deepening_search(graph: Maze, start, goal): 
    # Repeatedly depth-limit search till the maximum depth 
    paths_by_depth = []
    
    for lim in range(max_depth): 
        is_right, path = recursive_depth_limited_search(graph, start, goal, lim, expanded)
        if is_right: 
            paths_by_depth.append(path)
            break
        
    return paths_by_depth
