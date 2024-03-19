-- Sample data for Student table
INSERT INTO Student (Student_Number, Student_Name, Class, Major) VALUES
(1, 'John Doe', 'Senior', 'Computer Science'),
(2, 'Jane Smith', 'Junior', 'Electrical Engineering'),
(3, 'Alice Johnson', 'Sophomore', 'Mechanical Engineering');

-- Sample data for Course table
INSERT INTO Course (Course_Number, Course_Name, Credit_Hour, Department) VALUES
('CSCI101', 'Introduction to Computer Science', 3, 'Computer Science'),
('EE101', 'Introduction to Electrical Engineering', 4, 'Electrical Engineering'),
('MECH101', 'Advanced Mechanical Engineering', 4, 'Mechanical Engineering'),
('CSCI100', 'Introduction to Data Structure', 3, 'Computer Science'),
('EE100', 'Introduction to Basic Electrical', 4, 'Electrical Engineering'),
('MECH100', 'Introduction to Mechanical', 4, 'Mechanical Engineering');

-- Sample data for Section table
INSERT INTO Section (Section_Identifier, Course_Number, Semester, Year, Instructor) VALUES
('S1', 'CSCI101', 'Spring', 2023, 'Prof. Smith'),
('S2', 'MECH101', 'Spring', 2024, 'Prof. Lee'),
('S3', 'EE101', 'Spring', 2023, 'Prof. Brown'),
('S7', 'CSCI100', 'Fall', 2023, 'Prof. Smith'),
('S8', 'MECH100', 'Spring', 2024, 'Prof. Lee'),
('S9', 'EE100', 'Fall', 2023, 'Prof. Brown');


-- Sample data for Grade_Report table
INSERT INTO Grade_Report (Student_Number, Section_Identifier, Grade) VALUES
(1, 'S7', 'B'),
(2, 'S8', 'A'),
(3, 'S9', 'C'),
(1, 'S1', 'A'),
(2, 'S2', 'B'),
(3, 'S3', 'A');

-- Sample data for Prerequisite table
INSERT INTO Prerequisite (Course_Number, Prerequisite_Number) VALUES
('CSCI101', 'CSCI100'),
('EE101', 'EE100'),
('MECH101', 'MECH100');
