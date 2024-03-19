from flask import Blueprint, app, render_template, request
from sqlalchemy import text
from db import db

course_views = Blueprint('course_view', __name__)

@course_views.route('/course', methods=['GET', 'POST'])
def course_view():
    if request.method == 'POST':
        course_number = request.form['course_number']
        # Query to fetch grades for the given student_number
        query = text("""
            SELECT c.Course_Number, c.Course_Name, c.Credit_Hour, s.Semester, s.Year,c.Department, s.Instructor
            FROM Course c
            JOIN Section s ON c.Course_Number = s.Course_Number
            WHERE c.Course_Number = :course_number;
        """)
        courses = db.session.execute(query, {"course_number": course_number})
        return render_template('course.html', courses=courses, course_number=course_number)
    return render_template('course.html')

@course_views.route('/courses/all')
def all_courses():
    # Fetching data for all students
    query = text("""
            SELECT c.Course_Number, c.Course_Name, c.Credit_Hour,  s.Semester, s.Year, c.Department, s.Instructor
            FROM Course c
            JOIN Section s ON c.Course_Number = s.Course_Number
            """)

    courses =db.session.execute(query)
    return courses

@course_views.route('/courses/<course_number>')
def course_details(course_number):
    query = text("""
            SELECT c.Course_Number, c.Course_Name, c.Credit_Hour, s.Semester, s.Year,c.Department, s.Instructor
            FROM Course c
            JOIN Section s ON c.Course_Number = s.Course_Number
            WHERE c.Course_Number = :course_number;
        """)
    courses = db.session.execute(query, {"course_number": course_number})
    return render_template('course.html', courses=courses, course_number=course_number)
    