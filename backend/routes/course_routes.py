# Course Routes
# Author: Maryam Ghaffar
# Module: Course Management

from flask import Blueprint, request, jsonify
from backend.models.course import Course

course_bp = Blueprint('course', __name__)

# CREATE: Add a new course
@course_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400
    
    new_id = Course.create(
        data.get('title'),
        data.get('description', ''),
        data.get('teacher_id')
    )
    return jsonify({
        "message": "Course created successfully", 
        "course_id": new_id
    }), 201

# READ ALL: Get all courses
@course_bp.route('/courses', methods=['GET'])
def get_all_courses():
    return jsonify(Course.get_all()), 200

# READ ONE: Get a single course by ID
@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.get_by_id(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify(course), 200

# UPDATE: Edit an existing course
@course_bp.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400
    
    success = Course.update(
        course_id,
        data.get('title'),
        data.get('description', ''),
        data.get('teacher_id')
    )
    
    if success:
        return jsonify({"message": "Course updated successfully"}), 200
    return jsonify({"error": "Course not found"}), 404

# DELETE: Remove a course
@course_bp.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    success = Course.delete(course_id)
    
    if success:
        return jsonify({"message": "Course deleted successfully"}), 200
    return jsonify({"error": "Course not found"}), 404