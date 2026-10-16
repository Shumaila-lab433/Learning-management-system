# Course Model
# Author: Maryam Ghaffar
# Module: Course Management

class Course:
    def __init__(self, course_id, title, description, teacher_id):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.teacher_id = teacher_id

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "teacher_id": self.teacher_id
        }