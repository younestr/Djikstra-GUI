from queue import PriorityQueue   # manage nodes based on their distance from the start node.

def dijkstra(start, end, grid_size, obstacles): # starting & end node , obstacles on grid
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # directions on the grid: right, down, left, and up.
    pq = PriorityQueue()
    pq.put((0, start)) # start node init visited by 0 ( others with infinity )
    visited = set() # init of visited nodes
    previous = {start: None}
    
    while not pq.empty():  # main loop
        dist, current = pq.get()  # extraction of node with minimum distance
        if current in visited:
            continue      # skipping node if it's already visited to avoid extra calculations 
        visited.add(current) # marked as visited 
        
        if current == end:
            path = []
            while current:
                path.append(current)
                current = previous[current]  # checking if destination is reached
            path.reverse()
            return path        #  if current matches end node then it's the shortest path (return reconstructed end to start )
        
        row, col = current
        for dr, dc in directions:
            neighbor = (row + dr, col + dc)       # for each direction, a neighbor node is calculated. 
            if (0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size and 
                neighbor not in visited and neighbor not in obstacles): # checking the neighbor is within the grid, unvisited, and not an obstacle.
                pq.put((dist + 1, neighbor)) # adding neighbor to priority queue when valid
                previous[neighbor] = current
    return None  # path not found
