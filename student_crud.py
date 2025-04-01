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

def create_tables():
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


if __name__== "__main__":
    create_tables()
    insert_teacher("potato",20)
    