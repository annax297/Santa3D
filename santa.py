import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_santa():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Santa's face (sphere)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='peachpuff', alpha=1, edgecolor='none')

    # Santa's hat (cone)
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.linspace(0, 1, 50)
    R, T = np.meshgrid(r, theta)
    X = R * np.cos(T)
    Y = R * np.sin(T)
    Z = 1.5 - R  # Shift upwards
    ax.plot_surface(X, Y, Z, color='red', edgecolor='none')

    # Hat's pompom (small sphere)
    u_pom = np.linspace(0, 2 * np.pi, 50)
    v_pom = np.linspace(0, np.pi, 50)
    x_pom = 0.2 * np.outer(np.cos(u_pom), np.sin(v_pom))
    y_pom = 0.2 * np.outer(np.sin(u_pom), np.sin(v_pom))
    z_pom = 0.2 * np.outer(np.ones(np.size(u_pom)), np.cos(v_pom)) + 1.5
    ax.plot_surface(x_pom, y_pom, z_pom, color='white', edgecolor='none')

    # Santa's eyes (small spheres)
    for eye_pos in [(-0.3, 0.4), (0.3, 0.4)]:
        x_eye = 0.1 * np.outer(np.cos(u_pom), np.sin(v_pom)) + eye_pos[0]
        y_eye = 0.1 * np.outer(np.sin(u_pom), np.sin(v_pom)) + eye_pos[1]
        z_eye = 0.1 * np.outer(np.ones(np.size(u_pom)), np.cos(v_pom)) + 0.5
        ax.plot_surface(x_eye, y_eye, z_eye, color='black', edgecolor='none')

    # Santa's nose (small sphere)
    x_nose = 0.15 * np.outer(np.cos(u_pom), np.sin(v_pom))
    y_nose = 0.15 * np.outer(np.sin(u_pom), np.sin(v_pom))
    z_nose = 0.15 * np.outer(np.ones(np.size(u_pom)), np.cos(v_pom)) + 0.2
    ax.plot_surface(x_nose, y_nose, z_nose, color='red', edgecolor='none')

    # Santa's beard (lower hemisphere)
    u_beard = np.linspace(0, 2 * np.pi, 100)
    v_beard = np.linspace(0, np.pi / 2, 100)  # Only lower hemisphere
    x_beard = 1.2 * np.outer(np.cos(u_beard), np.sin(v_beard))
    y_beard = 1.2 * np.outer(np.sin(u_beard), np.sin(v_beard))
    z_beard = -1.2 * np.outer(np.ones(np.size(u_beard)), np.cos(v_beard))
    ax.plot_surface(x_beard, y_beard, z_beard, color='white', edgecolor='none')

    # Set the aspect ratio and labels
    ax.set_box_aspect([1, 1, 1])
    ax.axis('off')
    plt.show()

plot_santa()

