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

x, y = center, center

for step in range(10):
         dx,dy = move()
         x = x + dx
         y = y + dy
         print(x,y)


plt.imshow(grid, cmap="gray")
plt.show()




