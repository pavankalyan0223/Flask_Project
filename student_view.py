from flask import Blueprint, app, render_template, request
from sqlalchemy import text
from db import db

student_views = Blueprint('student_view', __name__)

@student_views.route('/student', methods=['GET', 'POST'])
def student_view():
    if request.method == 'POST':
        student_number = request.form['student_number']
        # Query to fetch grades for the given student_number
        query = text("""
            SELECT st.Student_Number,st.Student_Name,c.Course_Name,c.Course_Number,s.Section_Identifier,s.Instructor,c.Credit_Hour,s.Semester, s.Year, g.Grade 
            FROM 
               Student st
               JOIN Grade_Report g ON st.Student_Number = g.Student_Number
               JOIN Section s ON g.Section_Identifier = s.Section_Identifier
               JOIN Course c ON s.Course_Number = c.Course_Number
            WHERE 
               st.Student_Number = :student_number;
        """)
        grades = db.session.execute(query, {"student_number": student_number})
        return render_template('student.html', grades=grades, student_number=student_number)
    return render_template('student.html')

@student_views.route('/student/all')
def all_students_grades():
    # Fetching data for all students
    query = text("""
        SELECT st.Student_Number,st.Student_Name,c.Course_Name,c.Course_Number,s.Section_Identifier,s.Instructor,c.Credit_Hour,s.Semester, s.Year, g.Grade 
            FROM 
               Student st
               JOIN Grade_Report g ON st.Student_Number = g.Student_Number
               JOIN Section s ON g.Section_Identifier = s.Section_Identifier
               JOIN Course c ON s.Course_Number = c.Course_Number
            """)

    grades =db.session.execute(query)
    return grades


@student_views.route('/student/<student_number>')
def student_details(student_number):
    query = text("""
            SELECT st.Student_Number,st.Student_Name,c.Course_Name,c.Course_Number,s.Section_Identifier,s.Instructor,c.Department,c.Credit_Hour,s.Semester, s.Year, g.Grade 
            FROM 
               Student st
               JOIN Grade_Report g ON st.Student_Number = g.Student_Number
               JOIN Section s ON g.Section_Identifier = s.Section_Identifier
               JOIN Course c ON s.Course_Number = c.Course_Number
            WHERE 
               st.Student_Number = :student_number;
        """)
    grades = db.session.execute(query, {"student_number": student_number})
    return render_template('student.html', grades=grades ,student_number=student_number)
    