# plot_gui.py
import matplotlib.pyplot as plt
from tkinter import Tk, Button
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, radix_sort
from measure_performance import measure_sorting_algorithm, load_array
from array_generator import generate_random_array_file

import matplotlib.pyplot as plt

def plot_results(results):
    algorithms = list(results.keys())
    times = [results[algo]["time"] for algo in algorithms]
    spaces = [results[algo]["space"] for algo in algorithms]

    plt.figure(figsize=(12, 5))

    # Plot Time Complexity
    plt.subplot(1, 2, 1)
    plt.bar(algorithms, times, color='skyblue')
    plt.title("Time Complexity")
    plt.xlabel("Algorithms")
    plt.ylabel("Time (seconds)")

    # Plot Space Complexity
    plt.subplot(1, 2, 2)
    plt.bar(algorithms, spaces, color='salmon')
    plt.title("Space Complexity")
    plt.xlabel("Algorithms")
    plt.ylabel("Memory (bytes)")

    plt.tight_layout()
    plt.show()

def run_benchmark():
    # Step 1: Generate the random array file
    generate_random_array_file("random_array.txt", 1000, 100)  # Adjust size as needed

    # Step 2: Load the generated array from the file
    array = load_array("random_array.txt")
    results = {}

    # Step 3: Measure and record performance for each sorting algorithm
    for algo in [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, radix_sort]:
        try:
            time_taken, memory_used, _ = measure_sorting_algorithm(algo, array)
            if not isinstance(time_taken, (int, float)) or not isinstance(memory_used, (int, float)):
                print(f"Invalid data for {algo.__name__}")
                time_taken, memory_used = 0, 0  # Default to zero if invalid
            results[algo.__name__] = {"time": time_taken, "space": memory_used}
            print(f"{algo.__name__}: Time - {time_taken}, Space - {memory_used}")
        except Exception as e:
            print(f"Error with {algo.__name__}: {e}")
            results[algo.__name__] = {"time": 0, "space": 0}

    # Step 4: Save the sorted array to a file (optional)
    with open("sorted_array.txt", "w") as file:
        file.write("Sorting Benchmark Results\n")
        for algo_name, data in results.items():
            file.write(f"{algo_name}: Time - {data['time']}, Space - {data['space']}\n")

    # Step 5: Plot results using Matplotlib
    plot_results(results)



root = Tk()
root.title("Sorting Algorithm Performance Analyzer")
root.geometry("300x200")

Button(root, text="Run Benchmark", command=run_benchmark).pack(pady=20)

root.mainloop()
