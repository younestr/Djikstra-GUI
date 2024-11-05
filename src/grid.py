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
    
    def draw_grid(self):
        # Loop through your grid dimensions and draw the grid
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

    def get_cell_id(self, row, col):
        return row * self.grid_size + col + 1
    
    def place_start_node(self, event):
        # Logic to determine the grid position based on the click event
        row, col = self.get_grid_position(event.x, event.y)
        if not self.end_node and (row, col) not in self.obstacles:
            self.start_node = (row, col)
            self.draw_grid()  # Redraw to show start node

    def place_end_node(self, event):
        # Similar logic for placing end node
        row, col = self.get_grid_position(event.x, event.y)
        if not self.start_node and (row, col) not in self.obstacles:
            self.end_node = (row, col)
            self.draw_grid()  # Redraw to show end node

    def place_obstacle(self, event):
        # Logic for placing obstacles
        row, col = self.get_grid_position(event.x, event.y)
        if (row, col) != self.start_node and (row, col) != self.end_node:
            self.obstacles.add((row, col))
            self.draw_grid()  # Redraw to show obstacles

    def select_node(self, event):
        row, col = event.y // self.cell_size, event.x // self.cell_size
        if self.start_node is None:
            self.start_node = (row, col)
            self.canvas.itemconfig(self.get_cell_id(row, col), fill="green")
        elif self.end_node is None:
            self.end_node = (row, col)
            self.canvas.itemconfig(self.get_cell_id(row, col), fill="red")
        else:
            self.obstacles.add((row, col))
            self.canvas.itemconfig(self.get_cell_id(row, col), fill="gray")
    
    def reset(self):
        self.canvas.delete("all")  # Clear the canvas
        self.start_node = None      # Reset start node
        self.end_node = None        # Reset end node
        self.obstacles = set()      # Reset obstacles
        self.draw_grid()            # Redraw the grid
        
        # Resetting the status label and buttons
        self.status_label.config(text="Select start and end nodes")  # Reset status label
        self.run_button.config(state="normal")  # Enable run button
        self.reset_button.config(state="normal")  # Enable reset button

        # Allowing for new selections
        self.canvas.bind("<Button-1>", self.select_node)  # Re-bind click event to allow selections

    def mark_path(self, path):
        for (row, col) in path:
            if (row, col) not in [self.start_node, self.end_node]:
                self.canvas.itemconfig(self.get_cell_id(row, col), fill="blue")
