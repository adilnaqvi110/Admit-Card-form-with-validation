import psycopg2
import streamlit as st 

def get_db_connection():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="admit-card-form", 
            user="postgress", 
            password="postgres", 
            host="localhost", 
            port="5432"
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

def insert_student_data(student_data):
    conn = get_db_connection()
    if conn is None:
        return

    try:
        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Convert image files to binary format
        pass_photo_binary = student_data[4].getvalue() if student_data[4] else None
        signature_binary = student_data[5].getvalue() if student_data[5] else None

        # Execute a command: this inserts the data into the table
        insert_query = """
        INSERT INTO students (first_name, last_name, student_id, email, dob, pass_photo, signature)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (student_data[0], student_data[1], student_data[2], student_data[3], student_data[4], pass_photo_binary, signature_binary))

        # Commit the transaction
        conn.commit()

        st.success("Data successfully inserted into the database!")

    except Exception as e:
        st.error(f"Error inserting data: {e}")
    finally:
        # Close communication with the database
        cur.close()
        conn.close()
