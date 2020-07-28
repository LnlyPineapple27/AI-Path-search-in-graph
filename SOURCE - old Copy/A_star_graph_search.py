from Classes import Maze, Evaluation, ExploreFrontier, is_in_frontier

step_cost = 1

def A_star_graph_search(graph: Maze, start, goal):
    if goal == start:
        return [], []
    
    path = []
    path.append(start)
    path_heuristic = graph.manhattan_heuristic_calculator(start)

    expanded = []    
    frontier = []
    frontier.append(Evaluation(path_heuristic, path))
    
    while True:
        item = ExploreFrontier(frontier)# find the best next node to explore
        if item is None:
            break
        
        current_node = item.getFurthestNode()
        current_path = list(item.getPath())
        current_cost = item.getCost() - graph.manhattan_heuristic_calculator(current_node)
        expanded.append(current_node)
        
        # if goal was in frontier
        if current_node == goal:
            return expanded, current_path     
        
        nearby_nodes = (graph.getNode(current_node)).adjacent_list()
       
        for node in nearby_nodes:
            new_path = list(current_path)
            new_path.append(node)
            new_cost = current_cost + step_cost + graph.manhattan_heuristic_calculator(node)
            new_item = Evaluation(new_cost, new_path)
        
            location_in_frontier = is_in_frontier(node, frontier)
            if location_in_frontier is None:
                if node not in expanded:
                    frontier.append(new_item)
            else:
                # replace an existing frontier node which have higher cost
                if frontier[location_in_frontier].getCost() > new_cost:
                    frontier.pop(location_in_frontier)
                    frontier.append(new_item)
                    # no need to sort frontier 'cause ExploreFrontier can handle it 

    return None, None
    