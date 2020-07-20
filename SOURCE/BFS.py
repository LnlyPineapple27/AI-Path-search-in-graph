
def pop_frontier(frontier):
    if len(frontier) == 0:
        return None
    
    min_val = 10000 
    
    
    
def BFS_Search(graph, start, goal, board_size):
    path = []
    expanded_list = []
    
    if start == goal:
        return path, expanded_list
    
    path.append(start)
    
    frontier = [path]
    
    while len(frontier) > 0:
        cur_path = 
    