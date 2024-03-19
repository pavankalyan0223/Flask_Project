from flask import Flask, redirect, request, url_for, render_template
from student_view import student_views , all_students_grades
from course_view import course_views , all_courses
from instructor_view import instructor_views
from db import db,DATABASE_URI

app = Flask(__name__,template_folder='templates',static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db.init_app(app)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/student')
def student():
   grades=all_students_grades()
   return render_template('studentview.html',grades=grades)

@app.route('/courses')
def courses():
   courses=all_courses()
   return render_template('courseview.html',courses=courses)

app.register_blueprint(student_views)
app.register_blueprint(course_views)
app.register_blueprint(instructor_views)

if __name__ == '__main__':
   app.run(debug=True)