# measure_performance.py
import time
import os
import psutil

def load_array(filename):
    with open(filename, "r") as file:
        return list(map(int, file.read().split(",")))

import tracemalloc
import time

def measure_sorting_algorithm(algorithm, array):
    # Start tracking memory
    tracemalloc.start()
    # Measure time taken by the algorithm
    start_time = time.time()
    sorted_array = algorithm(array.copy())  # Pass a copy to avoid in-place sorting issues
    end_time = time.time()
    # Stop tracking memory and get memory usage
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time_taken = end_time - start_time
    memory_used = peak_memory

    return time_taken, memory_used, sorted_array
