from Classes import Maze, Node

# max_depth = 27
def recursive_depth_limited_search(graph: Maze, current_node: dict, goal, limit, expanded):
    expanded.append(current_node["Node"])
    if(current_node["Node"] == goal):
        return True, [current_node["Node"]]

    # If reached the depth limit, stop recursing. 
    if limit <= 0 : 
        return False, []
    
    node: Node = graph.getNode(current_node["Node"])
    nearby_nodes = node.adjacent_list()
    path = [current_node["Node"]]
    # Recur for all the vertices adjacent to this vertex 
    for item in nearby_nodes:       
        if item != current_node["Parent"]:
            next_node = {"Node" : item, "Parent" : current_node["Node"]}
            res, child_path = recursive_depth_limited_search(graph, next_node, goal, limit - 1, expanded)
            if(res): 
                return True, path + child_path
        
    return False, []
  
def Iterative_deepening_search(graph: Maze, start, goal): 
    # Repeatedly depth-limit search till the maximum depth 
    expanded_by_depth = []
    result_path = []
    size = graph.getSize()
    max_depth = size * size 
    for lim in range(0, max_depth): 
        expanded = []
        init_node = {"Node":start, "Parent": None}
        is_right, path = recursive_depth_limited_search(graph, init_node, goal, lim, expanded)
        expanded_by_depth.append(expanded)
        if is_right: 
            result_path = list(path)
            break
        
    return expanded_by_depth, result_path
    

