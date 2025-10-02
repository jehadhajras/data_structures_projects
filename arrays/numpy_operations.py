import numpy as np
import time

# ==============================
# Step 1: Compare List vs Array
# ==============================
elements = 1000000  # Use larger size to see performance difference

my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

# List time
list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"List Time: {time.time() - list_start:.5f}")

# Array time
array_start = time.time()
array_result = my_array1 + my_array2
print(f"Array Time: {time.time() - array_start:.5f}")

# Show only first 10 results (not all, to keep output clean)
print("First 10 results (List):", list_result[:10])
print("First 10 results (Array):", array_result[:10])

print("=" * 50)

# ==============================
# Step 2: Memory Usage
# ==============================
my_array = np.arange(100)

print("Array:", my_array)
print("Item Size:", my_array.itemsize)  # Bytes per element
print("Size:", my_array.size)           # Number of elements
print("All Bytes:", my_array.itemsize * my_array.size)

print("=" * 50)

# ==============================
# Step 3: Slicing
# ==============================
# index: 0    1    2    3    4
a = np.array(["A", "B", "C", "D", "E"])
print(a.ndim)
print(a[:])   # All items
print(a[1:2]) # B
print(a[:3])  # A, B, C
print(a[3:])  # D, E
print(a[::2]) # A, C, E
print(a[2::3])# C

print("=" * 50)

# 2D array slicing
b = np.array([
    ["A", "B", "X"], 
    ["C", "D", "Y"], 
    ["E", "F", "Z"], 
    ["M", "N", "O"]
])
print(b.ndim)
print("Row 2:", b[1])       # Whole second row
print("Even rows:", b[::2]) # Rows with step 2
print("All items:", b[:, :])
print("From col 1:", b[:, 1:])
print("Bottom right corner:", b[2:, 2:])
print("Specific column slice:", b[1:3, 1])

print("=" * 50)

# ==============================
# Step 4: Data Types
# ==============================
arr1 = np.array([1, 2, 3])
arr2 = np.array([20.3, 10.8, 0.3])
arr3 = np.array(["joe", "J", "Sam Hj"])

print(arr1.dtype) # int
print(arr2.dtype) # float
print(arr3.dtype) # string

# Type conversion
arr4 = np.array([1, 2, 3], dtype=float)
arr5 = np.array([20.3, 10.8, 0.3], dtype=int)

print(arr4.dtype) 
print(arr5.dtype) 

print("=" * 50)

# ==============================
# Step 5: Casting
# ==============================
arr6 = np.array([0, 1, 2, 3, 0, 4])
print("Original:", arr6, arr6.dtype)

arr6 = arr6.astype('float')
print("Float:", arr6, arr6.dtype)

arr6 = arr6.astype('bool')
print("Bool:", arr6, arr6.dtype)

print("=" * 50)

# ==============================
# Step 6: Arithmetic Operations
# ==============================
x = np.array([10, 20, 30])
y = np.array([5, 2, 4])

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print("#" * 50)

m1 = np.array([[1, 4], [5, 9]])
m2 = np.array([[2, 7], [10, 5]])

print(m1 + m2)
print(m1 - m2)
print(m1 * m2)
print(m1 / m2)

print("#" * 50)

# ==============================
# Step 7: Min, Max, Sum
# ==============================
arr7 = np.array([10, 20, 30])
print(arr7.min())
print(arr7.max())
print(arr7.sum())

arr8 = np.array([[6, 4], [3, 9]])
print(arr8.min())
print(arr8.max())
print(arr8.sum())

print("#" * 50)

# ==============================
# Step 8: Ravel and Reshape
# ==============================
arr9 = np.array([[6, 4], [3, 9]])
print("Flatten:", arr9.ravel())

arr10 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr10.ndim)
print("Flatten:", arr10.ravel())

# Shape and Reshape
arr11 = np.array([1, 2, 3, 4])
print(arr11.ndim, arr11.shape)

arr12 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr12.ndim, arr12.shape)

arr13 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshaped = arr13.reshape(3, 4)
print("Reshaped:", reshaped)
