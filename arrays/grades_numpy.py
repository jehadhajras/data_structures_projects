import numpy as np

# ========================================
# Example: Grades Management with NumPy Arrays
# ========================================

# Step 1: Create an array of student grades
grades = np.array([85, 90, 78, 92, 88, 82])
print("Original Grades:", grades)

print("=" * 40)

# Step 2: Access elements (first and last student's grade)
print("First student's grade:", grades[0])
print("Last student's grade:", grades[-1])

print("=" * 40)

# Step 3: Update a grade (student #3's grade from 78 → 80)
grades[2] = 80
print("Updated Grades:", grades)

print("=" * 40)

# Step 4: Calculate statistics
print("Average grade:", np.mean(grades))   # Mean
print("Highest grade:", np.max(grades))    # Max
print("Lowest grade:", np.min(grades))     # Min

print("=" * 40)

# Step 5: Add new students' grades (concatenation)
new_grades = np.array([95, 87])
grades = np.concatenate((grades, new_grades))
print("Grades after adding new students:", grades)

print("=" * 40)

# Step 6: Reshape grades (arrange into 2 rows for 2 classes)
reshaped = grades.reshape(2, -1)  # -1 lets NumPy figure out the right column size
print("Grades reshaped into 2 classes:\n", reshaped)

print("=" * 40)

# Step 7: Perform matrix-like operation (add bonus points to all students)
bonus = 2
grades_with_bonus = grades + bonus
print("Grades after adding bonus points:", grades_with_bonus)
