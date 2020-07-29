
#-----------------------------------Frontier_processing------------------

def is_in_frontier(node, frontier):
    for i in range(len(frontier)):
        temp = frontier[i]
        if temp["Node"] == node:
            return i
    return None

def ExploreFrontier(frontier_list):
    # this function will determine the node with lowest cost and number order to be explored next
    if frontier_list:
        possible_choice = []
        # a large random number is chosen for later comparison to get minimum value
        min = 99999*9999999

        for item in frontier_list:
            cur_cost = item["Cost"]
            if cur_cost < min: # if a shorter cost is found, update possible_path and min value
                min = cur_cost
                possible_choice.clear()
                possible_choice.append(item)
            elif cur_cost == min: # found another possible path with the same minimum cost
                possible_choice.append(item)
        if len(possible_choice) > 1:
            possible_choice = sorted(possible_choice, key = lambda i: i['Node']) # bring the path with lower number order to the top
            # print(possible_choice)
        best_result = possible_choice[0]
        frontier_list.remove(best_result) # remove the best result from frontier before exploring it
        return best_result
    return None

# -----------------------------------------------------
def tracePath(list_of_dict, start, goal): # list_of_dict must be valid to give correct result
    path = []
    tracing = goal
    if list_of_dict:
        for i in range(len(list_of_dict), 0, -1):
            if tracing is None:
              break
            cur = list_of_dict[i - 1]
            if cur["Node"] == tracing:
                path.append(cur["Node"])
                tracing = cur["Parent"]
                if cur["Node"] == start:
                    break
    path.reverse()# to get path from start to goal
    return path