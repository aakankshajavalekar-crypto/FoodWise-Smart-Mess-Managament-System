from database import get_connection


# =========================================================
# ADMIN LOGIN
# =========================================================

def admin_login(username, password):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT id, username
            FROM admin
            WHERE username = %s
              AND password = %s
            LIMIT 1
        """

        cursor.execute(
            query,
            (username.strip(), password)
        )

        return cursor.fetchone()

    except Exception as e:
        print("Admin Login Error:", e)
        return None

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


# =========================================================
# STUDENT REGISTER
# =========================================================

def register_student(student_id, password):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check existing student
        check_query = """
            SELECT id
            FROM students
            WHERE student_id = %s
            LIMIT 1
        """

        cursor.execute(
            check_query,
            (student_id.strip(),)
        )

        existing = cursor.fetchone()

        if existing:
            return False, "Student ID already exists."

        # Insert student
        insert_query = """
            INSERT INTO students
            (
                student_id,
                password
            )
            VALUES
            (
                %s,
                %s
            )
        """

        cursor.execute(
            insert_query,
            (
                student_id.strip(),
                password
            )
        )

        conn.commit()

        return True, "Student account created successfully."

    except Exception as e:

        if conn:
            conn.rollback()

        print("Student Registration Error:", e)

        return False, str(e)

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# =========================================================
# STUDENT LOGIN
# =========================================================

def student_login(student_id, password):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT
                id,
                student_id
            FROM students
            WHERE student_id = %s
              AND password = %s
            LIMIT 1
        """

        cursor.execute(
            query,
            (
                student_id.strip(),
                password
            )
        )

        return cursor.fetchone()

    except Exception as e:

        print("Student Login Error:", e)

        return None

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()