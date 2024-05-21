import random
import math
import numpy as np
from functools import reduce
from concurrent.futures import ProcessPoolExecutor
import time

def hypersphere_worker(n, d, r=1):
    points = np.random.uniform(-r, r, (n, d))
    distances = np.sum(points**2, axis=1)
    inside_circle = np.sum(distances <= r**2)
    return inside_circle

def hypersphere_parallel(n, d, num_processes, r=1):
    points_per_process = n // num_processes
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(hypersphere_worker, points_per_process, d, r) for _ in range(num_processes)]
        results = [future.result() for future in futures]
    
    total_inside_circle = sum(results)
    volume_approx = (2 * r) ** d * total_inside_circle / n
    
    return volume_approx

def hypersphere(n, d, r=1):
    points = np.random.uniform(-r, r, (n, d))
    distances = np.sum(points**2, axis=1)
    inside_sphere = np.sum(distances <= r**2)
    volume_approx = (2 * r) ** d * inside_sphere / n  
    return volume_approx

def hypersphere_exact(d, r=1):
    return (math.pi ** (d / 2) / math.gamma(d / 2 + 1)) * r ** d

def test():
    n_seq = 10000000
    n_par = 1000000
    d = 11
    num_processes = 10

    start_time = time.perf_counter()
    approx_volume_seq = hypersphere(n_seq, d)
    end_time = time.perf_counter()
    time_seq = end_time - start_time
 
    start_time = time.perf_counter()
    approx_volume_par = hypersphere_parallel(n_par * num_processes, d, num_processes)
    end_time = time.perf_counter()
    time_par = end_time - start_time

    exact_volume = hypersphere_exact(d)

    print(f"För sekventiell körning (n, d) = ({n_seq}, {d}):")
    print(f"Approximation av volym: {approx_volume_seq}")
    print(f"Exakt volym: {exact_volume}")
    print(f"Tid: {time_seq:.6f} sekunder\n")

    print(f"För parallell körning (n, d) = ({n_par * num_processes}, {d}) med {num_processes} processer:")
    print(f"Approximation av volym: {approx_volume_par}")
    print(f"Exakt volym: {exact_volume}")
    print(f"Tid: {time_par:.6f} sekunder\n")

    speedup = time_seq / time_par
    print(f"Parallell körning var {speedup:.2f} gånger snabbare än sekventiell körning.")


if __name__ == "__main__":
    test()