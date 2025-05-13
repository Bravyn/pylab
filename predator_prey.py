import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#parameters
alpha = 0.1
beta = 0.02
delta = 0.01
gamma = 0.1


#lotka-volterra system
def lokta_volterra(z, t):
    x, y = z 
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

#initial populations
x0 = 40
y0 = 9
z0 = [x0, y0]

#time points
t = np.linspace(0, 200, 1000)

#solve ODE
solution = odeint(lokta_volterra, z0, t)
x ,y = solution.T

#plot
plt.figure(figsize=(10, 5))

#population over time
plt.subplot(1, 2, 1)
plt.plot(t, x, label = 'Prey (Rabbits)', color = 'yellow')
plt.plot(t, y , label = 'Predators (Wolves)', color = 'red')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Predator-Prey Dynamics')
plt.legend()

#phase
plt.subplot(1, 2, 2)
plt.plot(x, y, color = 'purple')
plt.xlabel('Prey')
plt.ylabel('Predators')
plt.title('Phase Space (x vs. y)')


plt.tight_layout()
plt.show()