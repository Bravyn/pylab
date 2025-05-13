import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.widgets import Slider, Button

# Initial parameters
init_alpha = 0.1
init_beta = 0.02
init_delta = 0.01
init_gamma = 0.1

# Initial populations
x0 = 40
y0 = 9
z0 = [x0, y0]

# Time points
t = np.linspace(0, 200, 1000)

# ODE system
def lotka_volterra(z, t, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Plot setup
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
plt.subplots_adjust(bottom=0.35)

# Initial solution
solution = odeint(lotka_volterra, z0, t, args=(init_alpha, init_beta, init_delta, init_gamma))
x, y = solution.T

# Plot initial curves
time_line_prey, = ax[0].plot(t, x, label='Prey (Rabbits)', color='green')
time_line_pred, = ax[0].plot(t, y, label='Predators (Wolves)', color='red')
ax[0].legend()
ax[0].set_title("Population Over Time")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Population")

phase_line, = ax[1].plot(x, y, color='purple')
ax[1].set_title("Phase Space (Prey vs Predators)")
ax[1].set_xlabel("Prey")
ax[1].set_ylabel("Predators")

# Add sliders
ax_alpha = plt.axes([0.15, 0.25, 0.65, 0.03])
ax_beta = plt.axes([0.15, 0.20, 0.65, 0.03])
ax_delta = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_gamma = plt.axes([0.15, 0.10, 0.65, 0.03])

slider_alpha = Slider(ax_alpha, 'Prey Birth α', 0.01, 1.0, valinit=init_alpha)
slider_beta = Slider(ax_beta, 'Predation β', 0.001, 0.1, valinit=init_beta)
slider_delta = Slider(ax_delta, 'Predator Growth δ', 0.001, 0.1, valinit=init_delta)
slider_gamma = Slider(ax_gamma, 'Predator Death γ', 0.01, 1.0, valinit=init_gamma)

# Update function
def update(val):
    alpha = slider_alpha.val
    beta = slider_beta.val
    delta = slider_delta.val
    gamma = slider_gamma.val
    sol = odeint(lotka_volterra, z0, t, args=(alpha, beta, delta, gamma))
    x, y = sol.T
    time_line_prey.set_ydata(x)
    time_line_pred.set_ydata(y)
    phase_line.set_data(x, y)
    ax[0].relim(); ax[0].autoscale_view()
    ax[1].relim(); ax[1].autoscale_view()
    fig.canvas.draw_idle()

# Attach update to sliders
slider_alpha.on_changed(update)
slider_beta.on_changed(update)
slider_delta.on_changed(update)
slider_gamma.on_changed(update)

# Reset button
reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(reset_ax, 'Reset', color='lightgray', hovercolor='gray')

def reset(event):
    slider_alpha.reset()
    slider_beta.reset()
    slider_delta.reset()
    slider_gamma.reset()

reset_button.on_clicked(reset)

plt.show()
