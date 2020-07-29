from Classes import Maze
from Frontier_processing import ExploreFrontier, is_in_frontier, tracePath

step_cost = 1

def A_star_graph_search(graph: Maze, start, goal):
    if goal == start:
        return [goal], [goal]

    start_heuristic = graph.manhattan_heuristic_calculator(start)
    init = {"Node": start, "Parent": None, "Cost": start_heuristic}
    expanded = []
    expanded_with_parent = []
    frontier = []
    frontier.append(init)

    while True:
        item = ExploreFrontier(frontier)# find the best next node to explore
        if item is None:
            #print(expanded)
            break

        expanded.append(item["Node"])
        expanded_with_parent.append(item)

        # if goal was in frontier
        if item["Node"] == goal:
            current_path = tracePath(expanded_with_parent, start, item["Node"])
            return expanded, current_path
        
        current_cost = item["Cost"] - graph.manhattan_heuristic_calculator(item["Node"])
        nearby_nodes = (graph.getNode(item["Node"])).adjacent_list()

        for node in nearby_nodes:
            new_cost = current_cost + step_cost + graph.manhattan_heuristic_calculator(node)
            new_item = {"Node": node, "Parent": item["Node"], "Cost": new_cost}

            location_in_frontier = is_in_frontier(node, frontier)
            if location_in_frontier is None:
                if node not in expanded:
                    frontier.append(new_item)
            else:
                temp = frontier[location_in_frontier]
                if temp["Cost"] > new_item["Cost"]:
                    frontier.pop(location_in_frontier)
                    frontier.append(new_item)
                    # no need to sort frontier 'cause ExploreFrontier can handle it

    return expanded, None

    