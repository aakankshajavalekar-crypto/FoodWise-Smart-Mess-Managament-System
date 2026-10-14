USE smart_mess;

-- Your current students table already contains a password column.
-- For testing, set a password for an existing student record.
-- Replace the Student ID and password with your own values.

UPDATE students
SET password = 'student123',
    otp_verified = 1,
    otp = NULL,
    otp_expiry = NULL
WHERE student_id = '1';

-- Check the record after updating:
SELECT id, student_id, name, email, mobile, password, otp_verified
FROM students
WHERE student_id = '1';
