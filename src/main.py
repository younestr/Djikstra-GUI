import tkinter as tk
from grid import Grid
from dijkstra import dijkstra

class DijkstraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dijkstra's Algorithm Visualization")
        self.grid_size = 10
        self.cell_size = 30

        # Create the grid first and then pass button references
        self.grid = Grid(root, None, None, self.grid_size, self.cell_size)

        # Create buttons
        self.run_button = tk.Button(root, text="Run Dijkstra", command=self.run_dijkstra)
        self.reset_button = tk.Button(root, text="Reset", command=self.grid.reset)

        # Now update the grid with the button references
        self.grid.run_button = self.run_button
        self.grid.reset_button = self.reset_button

        # Bind the canvas click event
        self.grid.canvas.bind("<Button-1>", self.grid.select_node)

        # Pack the buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        self.run_button.pack(side="left", padx=5)
        self.reset_button.pack(side="left", padx=5)

    def run_dijkstra(self):
        if not self.grid.start_node or not self.grid.end_node:
            print("Please select start and end nodes.")
            return
        
        path = dijkstra(self.grid.start_node, self.grid.end_node, 
                        self.grid.grid_size, self.grid.obstacles)
        
        if path:
            self.grid.mark_path(path)
        else:
            print("No path found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DijkstraApp(root)
    root.mainloop()
