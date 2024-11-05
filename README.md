# Dijkstra's Algorithm Visualization

## How Dijkstra's Algorithm Works

Dijkstra's Algorithm is a popular algorithm used for finding the shortest paths between nodes in a graph. It works as follows:

1. **Initialization**: Set the distance to the starting node to 0 and all other nodes to infinity. Mark all nodes as unvisited. Create a priority queue to store nodes based on their distance.

2. **Visit Nodes**: While there are unvisited nodes:
   - Select the node with the smallest distance (the "current" node).
   - For each neighboring node, calculate the tentative distance through the current node. The formula to update the distance to a neighbor node, `i`, is:
     
     ```
     distance(node_i) = min(distance(node_i), distance(current) + cost(current, node_i))
     ```
     
     Here, `cost(current, node_i)` is the weight of the edge between the current node and `node_i`. If this distance is shorter than the previously recorded distance, we update it.

3. **Mark as Visited**: Once all neighbors have been considered, mark the current node as visited. A visited node will not be checked again.

4. **Repeat**: Repeat the process until all nodes have been visited or the shortest path to the destination node is found.

5. **Path Reconstruction**: After finishing, the algorithm can reconstruct the shortest path from the start node to the target node by backtracking from the target node to the start node.

The algorithm ensures that the shortest path is found efficiently, even in graphs with many nodes.

<div style="text-align: center;">
    <img src="Dijkstra_Animation.gif" alt="Dijkstra Animation" width="800" />
</div>

This animation demonstrates how Dijkstra's Algorithm works in real-time, showing the progression of node exploration and the final path calculation.

## Usage

- Click on a cell in the grid to set the starting node (green).
- Click on another cell to set the ending node (red).
- Click on cells to place obstacles (black).
- Press the "Run" button to execute Dijkstra's algorithm and visualize the shortest path (blue).
- Press the "Reset" button to clear the grid and start over.
