import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

class Particle:
  def __init__(self, position = None, velocity = None, acceleration = None):
    self.position = np.array(position if position is not None else [0, 0])
    self.acceleration = np.array(acceleration if acceleration is not None else [0, 0])
    self.velocity = np.array(velocity if velocity is not None else [0, 0])

  def update(self, dt): # semi-implicit Euler integration.
    self.velocity = self.velocity + self.acceleration * dt
    self.position = self.position + self.velocity * dt

p = Particle([0,0], [10,20], [0,-9.8])
dt = 0.1

pos = [] # this collects the trajectory points

while True:
  p.update(dt)
  if p.position[1] < 0:
      p.position[1] = 0
      pos.append(p.position.copy())
      break
  pos.append(p.position.copy())

xp = [p[0] for p in pos]
yp = [p[1] for p in pos]

# use this to see the analytical plot
'''plt.plot(xp, yp, marker = "o")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Particle Trajectory")
plt.show()'''

# Animation part
p = Particle([0,0], [10,20], [0,-9.8])
dt = 0.1

fig, ax = plt.subplots()
ax.set_xlim(0, 40)
ax.set_ylim(0, 25)

dot, = ax.plot([], [], 'ro', markersize = 8)

line, = ax.plot([], [], 'b-')

x_data, y_data = [], []
plt.close(fig)

def init(): # clears the particle’s position at the start of animation
    dot.set_data([], [])
    line.set_data([], [])
    return dot, line

def update(frame): # this fn updates the particle's frame
    p.update(dt)
    x_data.append(p.position[0])
    y_data.append(p.position[1])

    dot.set_data([p.position[0]], [p.position[1]])
    line.set_data(x_data, y_data)
    return dot,

anim = FuncAnimation(fig, update, frames=100, init_func=init, interval=50)
plt.close(fig)
HTML(anim.to_jshtml())