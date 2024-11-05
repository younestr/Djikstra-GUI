import tkinter as tk

class Grid:
    def __init__(self, root, grid_size=10, cell_size=30):
        self.root = root
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.start_node = None
        self.end_node = None
        self.obstacles = set()
        self.canvas = tk.Canvas(root, width=grid_size * cell_size, height=grid_size * cell_size)
        self.canvas.pack()

        self.draw_grid()
    
    def draw_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

    def get_cell_id(self, row, col):
        return row * self.grid_size + col + 1
    
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
        self.canvas.delete("all") # clear canvas
        self.start_node = None # reset start node
        self.end_node = None  # reset end node
        self.obstacles = set() # reset obstacles
        self.draw_grid()  # redraw the grid

    def mark_path(self, path):
        for (row, col) in path:
            if (row, col) not in [self.start_node, self.end_node]:
                self.canvas.itemconfig(self.get_cell_id(row, col), fill="blue")
