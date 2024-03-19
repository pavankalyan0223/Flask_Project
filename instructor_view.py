from flask import Blueprint, app, render_template, request
from sqlalchemy import text
from db import db

instructor_views = Blueprint('instructor_view', __name__)

@instructor_views.route('/instructor/<instructor_name>')
def instructor_details(instructor_name):
    # Query to fetch courses taught by the instructor
    query = text("""
        SELECT c.Course_Name, c.Course_Number, s.Section_Identifier, c.Credit_Hour, s.Semester, s.Year
        FROM Section s
        JOIN Course c ON s.Course_Number = c.Course_Number
        WHERE LOWER(s.Instructor) LIKE LOWER(:instructor_name);
    """)
    courses_taught = db.session.execute(query, {"instructor_name": f"%{instructor_name}%"})
    return render_template('instructor.html', instructor_name=instructor_name, courses_taught=courses_taught)