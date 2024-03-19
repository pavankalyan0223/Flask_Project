CREATE TABLE Student (
    Student_Number INT PRIMARY KEY,
    Student_Name VARCHAR(100),
    Class VARCHAR(50),
    Major VARCHAR(50)
);

CREATE TABLE Course (
    Course_Number INT PRIMARY KEY,
    Course_Name VARCHAR(100),
    Credit_Hour INT,
    Department VARCHAR(50)
);

CREATE TABLE Section (
    Section_Identifier INT PRIMARY KEY,
    Course_Number INT,
    Semester VARCHAR(20),
    Year INT,
    Instructor VARCHAR(100),
    FOREIGN KEY (Course_Number) REFERENCES Course(Course_Number)
);

CREATE TABLE Grade_Report (
    Student_Number INT,
    Section_Identifier INT,
    Grade CHAR(1),
    PRIMARY KEY (Student_Number, Section_Identifier),
    FOREIGN KEY (Student_Number) REFERENCES Student(Student_Number),
    FOREIGN KEY (Section_Identifier) REFERENCES Section(Section_Identifier)
);

CREATE TABLE Prerequisite (
    Course_Number INT,
    Prerequisite_Number INT,
    FOREIGN KEY (Course_Number) REFERENCES Course(Course_Number),
    FOREIGN KEY (Prerequisite_Number) REFERENCES Course(Course_Number)
);
