
from models.result import add_assessment
from models.student_result import (
    add_result,
    get_all_results,
    get_student_results,
    update_result
)

# Create a sample assessment
assessment_id = add_assessment(
    1, 101, "Database Assignment", "Assignment", 20
)

# Add student marks
result_id = add_result(assessment_id, 201, 17)

print("Student result added:", result_id)

# Get all results
print("\nAll Results:")
for result in get_all_results():
    print(dict(result))

# Get one student's results
print("\nStudent Results:")
for result in get_student_results(201):
    print(dict(result))

# Update marks
updated = update_result(result_id, 19)
print("\nMarks updated:", updated)

# Verify updated marks
print("Updated Result:", dict(get_all_results()[0]))
