import time
import random
import tracemalloc

# Quick Sort Implementation
import random
import sys
sys.setrecursionlimit(3000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def test_algorithms():
    sizes = [1000, 2000, 5000]
    for size in sizes:
        datasets = {
            "sorted": list(range(size)),
            "reverse": list(range(size, 0, -1)),
            "random": random.sample(range(size * 2), size)
        }
        for dtype, data in datasets.items():
            for algo_name, algo in [("Quick Sort", quick_sort), ("Merge Sort", merge_sort)]:
                data_copy = data.copy()
                tracemalloc.start()
                start_time = time.time()
                algo(data_copy)
                memory = tracemalloc.get_traced_memory()[1] / 1024  # peak memory in KB
                tracemalloc.stop()
                end_time = time.time()
                duration = (end_time - start_time) * 1000  # in milliseconds
                print(f"{algo_name} on {dtype} data of size {size}: {duration:.2f} ms, {memory:.2f} KB")

if __name__ == "__main__":
    test_algorithms()


