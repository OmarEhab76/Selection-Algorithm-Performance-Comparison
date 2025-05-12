# 🔍 Selection Algorithms Performance Comparison ⚡

## 📝 Project Overview
This Python script compares three algorithms for finding the k-th smallest element in an unsorted array.

## 🧮 Algorithms Implemented

1. **🔀 Merge Sort + Select (O(n log n))**
   - First sorts the entire array using merge sort
   - Then selects the k-th element in O(1)
   - ✅ Stable and deterministic
   - ❌ Inefficient for large data when only k-th element is needed
   - 💡 Best when array needs sorting anyway or for small arrays (n ≤ 1000)

2. **⚡ Quickselect (Average O(n), Worst O(n²))**
   - Selection algorithm based on quicksort
   - Recursively partitions without full sorting
   - ✅ Fastest for large datasets (n = 10,000 to 1,000,000)
   - ❌ Performance varies between runs due to random pivots
   - 💡 Ideal for real-time systems and large dataset analysis

3. **🎯 BFPRT/Median of Medians (Worst-case O(n))**
   - Deterministic selection algorithm
   - Uses median-of-medians for pivot selection
   - ✅ Guaranteed linear time
   - ❌ Slower for small/medium inputs due to extra computations
   - 💡 Best for highly skewed data or when worst-case guarantees matter

## 📊 Performance Comparison Summary

| Method          | Avg Time   | Worst Time | Best Use Cases                          |
|-----------------|------------|------------|-----------------------------------------|
| Merge Sort      | O(n log n) | O(n log n) | Small arrays or when sorting is needed  |
| Quickselect     | O(n)       | O(n²)      | General-purpose, large datasets         |
| BFPRT           | O(n)       | O(n)       | Worst-case guarantees, skewed data      |

## 🔍 Key Insights from Analysis

1. **Merge Sort Approach**:
   - "Computationally expensive since it sorts the array when we only care about the K-th element"
   - Only recommended when the array needs sorting anyway

2. **Quickselect Advantages**:
   - "Fastest for large n due to low overhead and in-place partitioning"
   - Preferred for real-time systems where average performance matters more than worst-case

3. **BFPRT Tradeoffs**:
   - "Guarantees worst-case linear time which quick selection can't do"
   - "Slower than quick selection for small to medium inputs" due to median computations

## 🚀 Benchmarking Approach
The script tests with array sizes from 100 to 1,000,000 elements:
- 🎲 Random array generation for each test size
- ⏱️ Measures median-finding time (k = n/2)
- 📊 Logarithmic scales for clear visualization
- 📈 Comparative performance plotting

## 🛠️ How to Run
```bash
python CompareAlgorithms.py
```

## 💡 Conclusion
1. Merge sort is **not ideal** for pure selection tasks
2. Quickselect is **best for performance** with large datasets
3. BFPRT provides **robust worst-case guarantees** but with added complexity

✨ "The choice depends on your specific needs: speed vs reliability vs simplicity" ✨
