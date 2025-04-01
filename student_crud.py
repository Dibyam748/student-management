import psycopg2
DB_NAME="postgres"
DB_USER="postgres.adfhdnejtqrbgrazyyxt"
DB_HOST="aws-0-ap-south-1.pooler.supabase.com"
DB_PASSWORD="QvRZrrrTpvybs6I9"
DB_PORT= 5432

def db_connection():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,host=DB_HOST, port=DB_PORT)
        print(conn)
        return conn
    except Exception as e:
        print("Error connecting to database:")
        return None

def create_teacher():
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS teacher (
                   id SERIAL PRIMARY KEY,
                   name VARCHAR(100) NOT NULL,
                   age INT NOT NULL)
        """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def insert_teacher(name,age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor. execute("INSERT INTO teacher (name,age) VALUES(%s,%s) RETURNING id",(name,age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted")

def update_teacher(name,age,id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor. execute("UPDATE teacher SET name= %s, age= %s WHERE id=%s",(name,age,id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data updated")

def delete_teacher(id):
    conn= db_connection()
    cursor = conn.cursor()
    cursor. execute("DELETE FROM teacher WHERE id= %s",(id,))
    conn. commit()
    cursor. close()
    conn. close()
    print("Data deleted")

def create_students():
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
        CREATE table IF NOT EXISTS students (
            student_id SERIAL  PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE,
            enrollment_date DATE DEFAULT CURRENT_DATE);
        """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def insert_student(first_name, last_name, email):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING student_id", 
                   (first_name, last_name, email))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted")

def update_student(id, name, age, department_id):
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute("""
        UPDATE students 
        SET name = %s, age = %s, department_id = %s 
        WHERE id = %s
    """, (name, age, department_id, id))
    connection.commit()
    print("Data updated")
    cursor.close()
    connection.close()

def delete_student(id):
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    connection.commit()
    print("Data deleted")
    cursor.close()
    connection.close()

def create_courses():
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS courses (
                    course_id SERIAL PRIMARY KEY,
                    course_name VARCHAR(100) NOT NULL,
                    department_id INT NOT NULL,
                    credits INT NOT NULL)
        """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def insert_course(course_name, department_id, credits):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (course_name, department_id, credits) VALUES (%s, %s, %s) RETURNING course_id", 
                   (course_name, department_id, credits))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted")

def update_course(id, name, credits):
    conn = db_connection()
    cursor=conn.cursor()
    cursor. execute("""
        UPDATE courses 
        SET name = %s, credits = %s 
        WHERE id = %s
    """, (name, credits, id))
    connection.commit()
    print("Data updated")
    cursor.close()
    connection.close()


def delete_course(id):
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = %s", (id,))
    connection.commit()
    print("Data deleted")
    cursor.close()
    connection.close()

def create_enrollment():
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS enrollments(
                enrollment_id SERIAL PRIMARY KEY,
                student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
                teacher_id INT REFERENCES teacher(id) ON DELETE CASCADE,
                course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
                grade VARCHAR(2));
        """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def insert_enrollment(student_id, teacher_id, course_id, grade):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(""" 
        INSERT INTO enrollments (student_id, teacher_id, course_id, grade) 
        VALUES (%s, %s, %s, %s) RETURNING enrollment_id""", 
        (student_id, teacher_id, course_id, grade))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted")


def update_enrollment(id, student_id, course_id):
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute("""
        UPDATE enrollments 
        SET student_id = %s, course_id = %s 
        WHERE id = %s
    """, (student_id, course_id, id))
    connection.commit()
    print("Data updated")
    cursor.close()
    connection.close()

def delete_enrollment(id):
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM enrollments WHERE id = %s", (id,))
    connection.commit()
    print("Data deleted")
    cursor.close()
    connection.close()


def create_departments():
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS departments(
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(100) NOT NULL);
        """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table Created")

def insert_department(department_name):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO departments (department_name) VALUES (%s) RETURNING department_id", (department_name,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted")


def update_department(id, name):
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute("""
        UPDATE departments 
        SET name = %s 
        WHERE id = %s
    """, (name, id))
    connection.commit()
    print("Data updated")
    cursor.close()
    connection.close()

def delete_department(id):
    conn = db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM departments WHERE id = %s", (id,))
    connection.commit()
    print("Data deleted")
    cursor.close()
    connection.close()

if __name__== "__main__":
    create_enrollment()
    insert_enrollment(1,4,1,'A')