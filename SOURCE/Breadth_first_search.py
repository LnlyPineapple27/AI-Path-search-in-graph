from Classes import Maze, tracePath

def Breadth_first_search(graph: Maze, start, goal):
    expanded = []
    expanded_with_parent = []
    frontier = []
    # dict format: { "Node": 2, "Parent": 1 },
    init = {"Node": start, "Parent": None}
    frontier.append(init)
    # return nothing if goal is start
    if start == goal:
        return [], []

    while frontier:
        current_node = frontier.pop(0)
        node = current_node["Node"]
        if node not in expanded:
            neighbours = (graph.getNode(node)).adjacent_list()
            for neighbour in neighbours:
                if neighbour == goal:
                    expanded.append(node)
                    expanded.append(goal)
                    expanded_with_parent.append(current_node)
                    expanded_with_parent.append({"Node": goal, "Parent": node})

                    path_to_node = tracePath(expanded_with_parent, start, neighbour)
                    return expanded, path_to_node
                else:
                    new_node = {"Node": int(neighbour), "Parent": node}
                    frontier.append(new_node)
            expanded.append(node)
            expanded_with_parent.append(current_node)

    return None, None
