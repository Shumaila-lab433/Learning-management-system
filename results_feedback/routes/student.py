
from flask import Blueprint, render_template, request

from models.student_result import get_student_results
from models.feedback import get_student_feedback

student = Blueprint("student", __name__, url_prefix="/student")


@student.route("/results")
def results():
    student_id = request.args.get("student_id", 201, type=int)
    results_list = get_student_results(student_id)

    return render_template(
        "student/results.html",
        results=results_list
    )


@student.route("/feedback")
def feedback():
    student_id = request.args.get("student_id", 201, type=int)
    feedback_list = get_student_feedback(student_id)

    return render_template(
        "student/feedback.html",
        feedback_list=feedback_list
    )
