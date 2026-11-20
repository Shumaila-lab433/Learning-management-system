
from db import get_db


def add_assessment(course_id, teacher_id, title, assessment_type, total_marks, due_date=None):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO assessments
        (course_id, teacher_id, title, assessment_type, total_marks, due_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (course_id, teacher_id, title, assessment_type, total_marks, due_date))

    connection.commit()
    assessment_id = cursor.lastrowid
    connection.close()

    return assessment_id


def get_all_assessments():
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM assessments ORDER BY assessment_id DESC")
    assessments = cursor.fetchall()

    connection.close()
    return assessments


def get_assessment_by_id(assessment_id):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM assessments WHERE assessment_id = ?",
        (assessment_id,)
    )

    assessment = cursor.fetchone()
    connection.close()

    return assessment


def delete_assessment(assessment_id):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM assessments WHERE assessment_id = ?",
        (assessment_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()

    return deleted
