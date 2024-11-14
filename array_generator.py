# array_generator.py
import random

def generate_random_array_file(filename, size, max_value):
    array = [random.randint(1, max_value) for _ in range(size)]
    with open(filename, "w") as file:
        file.write(",".join(map(str, array)))

# Generate a random array file with 1000 elements ranging from 1 to 100
generate_random_array_file("random_array.txt", 1000, 100)
