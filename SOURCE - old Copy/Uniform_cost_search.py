from Classes import Maze, Evaluation, ExploreFrontier, is_in_frontier

step_cost = 1

def Uniform_cost_search(graph: Maze, start, goal):
    if goal == start:
        return [], []
    
    path_cost = 0
    path = []
    path.append(start)
    expanded = []    
    frontier = []
    frontier.append(Evaluation(path_cost, path))
    
    while True:
        item = ExploreFrontier(frontier)
        if item is None:
            break
        
        current_node = item.getFurthestNode()
        current_path = list(item.getPath())
        current_cost = item.getCost()
        # print(current_path)
        expanded.append(current_node)
        
        # if goal was in frontier
        if current_node == goal:
            return expanded, current_path     
        
        nearby_nodes = (graph.getNode(current_node)).adjacent_list()
    
        for node in nearby_nodes:
            new_path = list(current_path)
            new_path.append(node)
            new_cost = current_cost + step_cost
            new_item = Evaluation(new_cost, new_path)
        
            in_frontier = is_in_frontier(node, frontier)
            if in_frontier is None:
                if node not in expanded:
                    frontier.append(new_item)
            else:
                if frontier[in_frontier].getCost() > new_cost:
                    frontier.pop(in_frontier)
                    frontier.append(new_item)
                    # no need to sort frontier 'cause ExploreFrontier can handle it
    
    return None, None
    