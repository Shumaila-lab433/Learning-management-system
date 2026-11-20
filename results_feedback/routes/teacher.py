
from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.result import add_assessment, get_all_assessments
from models.student_result import add_result, get_all_results
from models.feedback import add_feedback, get_all_feedback

teacher = Blueprint("teacher", __name__, url_prefix="/teacher")


@teacher.route("/dashboard")
def dashboard():
    return render_template("teacher/dashboard.html")


@teacher.route("/add-result", methods=["GET", "POST"])
def add_student_result():
    if request.method == "POST":
        assessment_id = request.form["assessment_id"]
        student_id = request.form["student_id"]
        marks = request.form["obtained_marks"]

        add_result(assessment_id, student_id, marks)
        flash("Student result added successfully!")

        return redirect(url_for("teacher.manage_results"))

    assessments = get_all_assessments()
    return render_template("teacher/add_result.html", assessments=assessments)


@teacher.route("/manage-results")
def manage_results():
    results = get_all_results()
    return render_template("teacher/manage_results.html", results=results)


@teacher.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        add_feedback(
            request.form["student_id"],
            request.form["teacher_id"],
            request.form["course_id"],
            request.form["message"]
        )
        flash("Feedback added successfully!")
        return redirect(url_for("teacher.feedback"))

    feedback_list = get_all_feedback()
    return render_template(
        "teacher/feedback.html",
        feedback_list=feedback_list
    )
