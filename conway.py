import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#grid size
GRID_SIZE =50

#probability a cell starts alive
INITIAL_DENSITY = 0.2

#Initialize the grid with random True (alive) or False (dead) values
def create_grid():
    return np.random.rand(GRID_SIZE, GRID_SIZE) < INITIAL_DENSITY

#count live neighbors(grid) 
def count_neighbors(grid, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            xi = (x + i) % GRID_SIZE
            xj = (y + j) % GRID_SIZE
            total += grid[xi, xj]
    return total

#update grid based on rules
def update(frame_num, img, grid):
    new_grid = grid.copy()
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            neighbors = count_neighbors(grid, x, y)
            if grid[x , y] and (neighbors < 2 or neighbors > 3):
                new_grid[x, y] = False
            elif not grid[x, y] and neighbors == 3:
                new_grid[x, y] = True

    img.set_data(new_grid)
    grid[:] = new_grid
    return img,

#init
grid = create_grid()
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), interval = 100, save_count=50)

plt.title("Conway's Game of Life")
plt.axis('off')
plt.show()