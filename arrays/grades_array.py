import array

# ----------------------------
# Example: Working with grades using array
# ----------------------------

# Create an array of integer grades
grades = array.array('i', [85, 90, 78, 92, 88])

# Print grades
print(f"Grades: {grades.tolist()}")

# Access grades by index
print(f"First Grade: {grades[0]}")
print(f"Last Grade: {grades[-1]}")

# Update a grade
prev_grade = grades[2]
grades[2] = 80
new_grade = grades[2]
print(f"Grade {prev_grade} has successfully updated to {new_grade}.")
print(f"All Grades: {grades.tolist()}")

# Insert a new grade
grades.insert(2, 70)
print(f"After insertion: {grades.tolist()}")

# Delete a grade
grades.remove(90)
print(f"After Deletion: {grades.tolist()}")

# Search for a grade
search_value = 80
if search_value in grades:
    print(f"Found grade: {search_value}")
else:
    print(f"Grade {search_value} Not found.")

# Final grades
print(f"Final Grades: {grades.tolist()}")
