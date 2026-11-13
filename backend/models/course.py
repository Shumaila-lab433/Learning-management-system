# Course Model
# Author: Maryam Ghaffar
# Module: Course Management

from backend.utils.database import get_connection

class Course:
    @staticmethod
    def create(title, description, teacher_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO courses (title, description, teacher_id) VALUES (?, ?, ?)",
            (title, description, teacher_id)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses ORDER BY course_id DESC")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @staticmethod
    def get_by_id(course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE course_id = ?", (course_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @staticmethod
    def update(course_id, title, description, teacher_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE courses SET title = ?, description = ?, teacher_id = ? WHERE course_id = ?",
            (title, description, teacher_id, course_id)
        )
        conn.commit()
        rows = cursor.rowcount
        conn.close()
        return rows > 0

    @staticmethod
    def delete(course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE course_id = ?", (course_id,))
        conn.commit()
        rows = cursor.rowcount
        conn.close()
        return rows > 0