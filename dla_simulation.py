import numpy as np
import matplotlib.pyplot as plt
import random

grid_size = 300
num_particles = 4000
sticking_probality = 1.0 #sigma

grid=np.zeros((grid_size,grid_size))

print(grid_size)
print(num_particles)
print(sticking_probality)
print(grid)

center = grid_size // 2
grid[center, center] = 1

def move():
    return random.choice([(-1,0),(1,0),(0,-1),(0,1)])


for particle in range(num_particles):
    x, y = center, center
    for step in range(100000):
        dx,dy = move()
        x = x + dx
        y = y + dy
        print(x,y)
        if grid[x-1,y]== 1 or grid[x+1, y] == 1 or grid[x, y-1] == 1 or grid[x, y+1] == 1:
               grid[x,y] = 1
               print("particle stuck at" , x, y)
               break


plt.imshow(grid, cmap="gray")
plt.show()




