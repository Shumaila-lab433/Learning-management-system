
from models.feedback import (
    add_feedback,
    get_student_feedback,
    get_all_feedback,
    delete_feedback
)

# Add feedback
feedback_id = add_feedback(
    student_id=201,
    teacher_id=101,
    course_id=1,
    message="Good work! Keep improving."
)

print("Feedback added:", feedback_id)

# Get student feedback
print("\nStudent Feedback:")
for item in get_student_feedback(201):
    print(dict(item))

# Get all feedback
print("\nAll Feedback:")
for item in get_all_feedback():
    print(dict(item))

# Delete feedback
deleted = delete_feedback(feedback_id)
print("\nFeedback deleted:", deleted)
