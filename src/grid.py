import tkinter as tk

class Grid:
    def __init__(self, root, run_button, reset_button, grid_size=10, cell_size=30):
        self.root = root
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.start_node = None
        self.end_node = None
        self.obstacles = set()
        self.canvas = tk.Canvas(root, width=grid_size * cell_size, height=grid_size * cell_size)
        self.canvas.pack()

        # Create a status label
        self.status_label = tk.Label(root, text="Select start and end nodes")
        self.status_label.pack()

        # Store button references
        self.run_button = run_button
        self.reset_button = reset_button

        self.draw_grid()

        # Bind the click event for selecting nodes
        self.canvas.bind("<Button-1>", self.select_node)

    def draw_grid(self):
        self.canvas.delete("all")  # Clear previous drawings
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Logic to determine cell color based on obstacles, start, and end nodes
                if (row, col) in self.obstacles:
                    color = "black"  # Color for obstacles
                elif (row, col) == self.start_node:
                    color = "green"  # Color for start node
                elif (row, col) == self.end_node:
                    color = "red"    # Color for end node
                else:
                    color = "white"  # Default color for free cells
                self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size,
                                            (col + 1) * self.cell_size, (row + 1) * self.cell_size,
                                            fill=color, outline="gray")

    def select_node(self, event):
        row, col = event.y // self.cell_size, event.x // self.cell_size
        
        if self.start_node is None:  # selecting start node
            if (row, col) not in self.obstacles:  # prevent placing start node on obstacles
                self.start_node = (row, col)
                self.draw_grid()  # redraw to show start node
                self.status_label.config(text="Select end node")
        elif self.end_node is None:  # selecting end node
            if (row, col) not in self.obstacles:  # prevent placing end node on obstacles
                self.end_node = (row, col)
                self.draw_grid()  # redraw to show end node
                self.status_label.config(text="Click to place obstacles or run the algorithm")
        else:  # placing obstacles
            if (row, col) != self.start_node and (row, col) != self.end_node:
                self.obstacles.add((row, col))
                self.draw_grid()  # redraw to show obstacles

    def reset(self):
        self.start_node = None      # reset start node
        self.end_node = None        # reset end node
        self.obstacles = set()      # reset obstacles
        self.draw_grid()            # redraw the grid
        
        # resetting the status label and buttons
        self.status_label.config(text="Select start and end nodes")  # reset status label
        self.run_button.config(state="normal")  # enable run button
        self.reset_button.config(state="normal")  # enable reset button

        # re-bind the click event for selections
        self.canvas.bind("<Button-1>", self.select_node)

    def mark_path(self, path):
        for (row, col) in path:
            if (row, col) not in [self.start_node, self.end_node]:
                self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size,
                                              (col + 1) * self.cell_size, (row + 1) * self.cell_size,
                                              fill="blue", outline="gray")  # draw the path
