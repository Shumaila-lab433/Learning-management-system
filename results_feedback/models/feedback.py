
from db import get_db


def add_feedback(student_id, teacher_id, course_id, message):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO feedback
        (student_id, teacher_id, course_id, message)
        VALUES (?, ?, ?, ?)
    """, (student_id, teacher_id, course_id, message))

    connection.commit()
    feedback_id = cursor.lastrowid
    connection.close()

    return feedback_id


def get_student_feedback(student_id):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM feedback
        WHERE student_id = ?
        ORDER BY feedback_id DESC
    """, (student_id,))

    feedback = cursor.fetchall()
    connection.close()

    return feedback


def get_all_feedback():
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM feedback ORDER BY feedback_id DESC")
    feedback = cursor.fetchall()

    connection.close()
    return feedback


def delete_feedback(feedback_id):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM feedback WHERE feedback_id = ?",
        (feedback_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()

    return deleted
