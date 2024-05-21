import random
import math
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

def pi_points(n):
    inside_circle = 0
    points_inside = []
    points_outside = []

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            points_inside.append((x, y))
        else:
            points_outside.append((x, y))

    return inside_circle, points_inside, points_outside

def pi_circle(total_points, num_threads):
    points_per_thread = total_points // num_threads
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(pi_points, points_per_thread) for _ in range(num_threads)]
        
        total_inside_circle = 0
        all_points_inside = []
        all_points_outside = []

        for future in futures:
            inside_circle, points_inside, points_outside = future.result()
            total_inside_circle += inside_circle
            all_points_inside.extend(points_inside)
            all_points_outside.extend(points_outside)

    pi_approx = 4 * total_inside_circle / total_points

    print(f"Antal punkter i cirkeln: {total_inside_circle}")
    print(f"Approximation av pi: {pi_approx}")
    print(f"Inbyggd konstant pi: {math.pi}")

    fig, ax = plt.subplots()
    if all_points_inside:
        x_inside, y_inside = zip(*all_points_inside)
        ax.scatter(x_inside, y_inside, color='red', s=1)
    if all_points_outside:
        x_outside, y_outside = zip(*all_points_outside)
        ax.scatter(x_outside, y_outside, color='blue', s=1)

    ax.set_aspect('equal')
    plt.savefig("pi_circle.png")
    plt.show()


pi_circle(100000, 4)