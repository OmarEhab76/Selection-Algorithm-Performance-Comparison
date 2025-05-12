import random
import time
import matplotlib.pyplot as plt

# --- Custom Merge Sort ---
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# --- Method 1: Merge Sort + Select kth ---
def kth_smallest_merge(arr, k):
    return merge_sort(arr)[k - 1]

# --- Method 2: Quickselect ---
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k <= len(lows):
        return quickselect(lows, k)
    elif k > len(lows) + len(pivots):
        return quickselect(highs, k - len(lows) - len(pivots))
    else:
        return pivots[0]

# --- Method 3: BFPRT ---
def bfprt_select(arr, k):
    def partition(arr, pivot):
        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]
        return lows, pivots, highs

    def select(arr, k):
        if len(arr) <= 5:
            return sorted(arr)[k]
        medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]
        pivot = select(medians, len(medians) // 2)
        lows, pivots, highs = partition(arr, pivot)
        if k < len(lows):
            return select(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return select(highs, k - len(lows) - len(pivots))
    return select(arr, k - 1)

# --- Benchmarking ---
sizes = [100, 1000, 10000, 100000, 1000000]
results = {"n": [], "merge_time": [], "quick_time": [], "bfprt_time": []}

for n in sizes:
    array = [random.randint(1, 10**6) for _ in range(n)]
    k = n // 2

    # Time Merge Sort
    start = time.time()
    kth_smallest_merge(array[:], k)
    results["merge_time"].append(time.time() - start)

    # Time Quickselect
    start = time.time()
    quickselect(array[:], k)
    results["quick_time"].append(time.time() - start)

    # Time BFPRT
    start = time.time()
    bfprt_select(array[:], k)
    results["bfprt_time"].append(time.time() - start)

    results["n"].append(n)

# --- Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(results["n"], results["merge_time"], marker='o', label="Merge Sort (O(n log n))", linestyle='--')
plt.plot(results["n"], results["quick_time"], marker='s', label="Quickselect (Avg O(n))", linestyle='-')
plt.plot(results["n"], results["bfprt_time"], marker='^', label="BFPRT (Worst-case O(n))", linestyle='-.')

plt.xscale('log')
plt.yscale('log')
plt.xlabel("Array Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Selection Algorithms: Performance Comparison")
plt.legend()
plt.grid(True, which="both", linestyle='--')
plt.tight_layout()
plt.show()
