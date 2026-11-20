
from db import get_db


# Add student marks
def add_result(assessment_id, student_id, obtained_marks):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO results
        (assessment_id, student_id, obtained_marks)
        VALUES (?, ?, ?)
    """, (assessment_id, student_id, obtained_marks))

    connection.commit()
    result_id = cursor.lastrowid
    connection.close()

    return result_id


# Get all student results
def get_all_results():
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM results
        ORDER BY result_id DESC
    """)

    results = cursor.fetchall()
    connection.close()

    return results


# Get results for one student
def get_student_results(student_id):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT results.*, assessments.title,
               assessments.total_marks,
               assessments.assessment_type
        FROM results
        JOIN assessments
        ON results.assessment_id = assessments.assessment_id
        WHERE results.student_id = ?
        ORDER BY results.result_id DESC
    """, (student_id,))

    results = cursor.fetchall()
    connection.close()

    return results


# Update student marks
def update_result(result_id, obtained_marks):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE results
        SET obtained_marks = ?
        WHERE result_id = ?
    """, (obtained_marks, result_id))

    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()

    return updated

