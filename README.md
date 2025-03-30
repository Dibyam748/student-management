# student-management
CREATE table students (
  student_id SERIAL  PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  enrollment_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE courses (
  course_id SERIAL PRIMARY KEY,
  course_name VARCHAR(100) NOT NULL,
  department_id INT,
  credits INT NOT NULL
);

CREATE TABLE enrollments(
  enrollment_id SERIAL PRIMARY KEY,
  student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
  course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
  grade VARCHAR(2)
);

CREATE TABLE departments(
  department_id SERIAL PRIMARY KEY,
  department_name VARCHAR(100) NOT NULL
);

INSERT INTO students(first_name,last_name,email,enrollment_date) VALUES
('Abhishrek','Thapa','shrek123@gmail.com','2023-04-01'),
('Diplal','Karki','diplal123@gmail.com','2024-04-01'),
('Manoj','Singh','manojwow@gmail.com','2023-04-01'),
('Hehe','Basnet','hehe123@gmail.com','2024-04-01'),
('Abiral','Adhikari','abiralgamer@gmail.com','2023-04-01');

INSERT INTO courses (course_name,department_id,credits)
values
('Python',1,10),
('JavaScript',1,8),
('Statistics',2,12);  

INSERT INTO enrollments
(student_id, course_id, grade )
VALUES(1, 1, 'A'),
(2, 2, 'A'),
(3, 3, 'F'),
(4, 2, 'C'),
(5, 1, 'A');

INSERT INTO departments
(department_name)
VALUES
('Computer Science'),
('Mathematics');
