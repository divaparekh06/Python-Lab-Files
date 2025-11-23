# import sqlite3
# # Connect to database (or create it)
# conn = sqlite3.connect('student_record.db')
# # Create a cursor object using the cursor() method
# cursor = conn.cursor()

# # Create students table if it doesn't exist
# cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
#                     Enrollment INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     Subject TEXT NOT NULL,
#                     Mark INTEGER NOT NULL
#                 )''')


# # Commit the changes
# conn.commit()
# # Insert multiple employee records
# student_record = [
#     (92301733016,'ASHUTOSH KUMAR SINGH','PWP',95),
#     (92301733017,'HARSH VISHALBHAI TRIVEDI','PWP',85),
#     (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','PWP',90),
#     (92301733046,'SHIVAM ATULKUMAR BHATT', 'PWP',93),
#     (92301733058,'DEVENDRASINH DOLATSINH JADEJA','PWP',75)
# ]
# # Using executemany to insert multiple records
# cursor.executemany('''INSERT INTO student_record (Enrollment, name, subject,Mark) 
#                       VALUES (?, ?, ?,?)''', student_record)

# # Commit the changes
# conn.commit()

# # Fetch all student records
# cursor.execute('SELECT * FROM student_record')
# rows = cursor.fetchall()
# # Display the results
# print("All Student Records:")
# for row in rows:
#     print(row)
    
# # Fetch student got more than 90
# cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Mark > 90')
# high_marks = cursor.fetchall()

# print("\nStudents with Marks greater than 90:")
# for student in high_marks:
#     print(student)
    
# # Fetch student got more than 90
# cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Mark > 90')
# high_marks = cursor.fetchall()

# print("\nStudents with Marks greater than 90:")
# for student in high_marks:
#     print(student)


# # Update MArk for Ashutosh kumar (PWP)
# cursor.execute('''UPDATE student_record SET Mark = 98 
#                   WHERE name = 'ASHUTOSH KUMAR SINGH' AND subject = 'PWP' ''')

# # Commit the changes
# conn.commit()
# # Verify the update
# cursor.execute('SELECT name, MArk FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
# updated_mark = cursor.fetchone()
# print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")
# # Delete a student record (e.g.,DEVENDRASINH DOLATSINH JADEJA )
# cursor.execute('''DELETE FROM student_record WHERE name = 'DEVENDRASINH DOLATSINH JADEJA' ''')

# # Commit the changes
# conn.commit()

# # Verify the deletion
# cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
# deleted_name = cursor.fetchone()

# if deleted_name is None:
#     print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")
# # Calculate the average Mark
# cursor.execute('''SELECT AVG(Mark) FROM student_record''')
# avg_mark = cursor.fetchone()[0]

# print(f"\nThe average mark of students is: ${avg_mark:.2f}")
# # Close the connection
# conn.close()



#---------------POST LABS--------------
import sqlite3 
# Connect to database (or create it) 
conn = sqlite3.connect('multiple_student_subjects.db') 
# Create a cursor object using the cursor() method 
cursor = conn.cursor() 
 
# Drop old table for clean start 
cursor.execute('DROP TABLE IF EXISTS multiple_student_subjects') 
 
# Create table with composite primary key 
cursor.execute(''' 
    CREATE TABLE multiple_student_subjects ( 
        Enrollment INTEGER, 
        name TEXT NOT NULL, 
        Subject TEXT NOT NULL, 
        Mark INTEGER NOT NULL, 
        PRIMARY KEY (Enrollment, Subject)
) 
''') 
conn.commit() 
# Student records 
multiple_student_subjects = [ 
(92400133161, 'Diva', 'PWP', 99), 
(92400133161, 'Diva', 'DMGT', 99), 
(92400133161, 'Diva', 'ICE', 99), 
(92400133161, 'Diva', 'DSC', 99), 
(92400133161, 'Diva', 'SS', 99), 
(92400133161, 'Diva', 'SPDT', 99), 
(92400133161, 'Diva', 'APTI', 99), 
(92400133161, 'Diva', 'COA', 99) 
] 
cursor.executemany('''  
INSERT INTO multiple_student_subjects (Enrollment, name, Subject, Mark)  
VALUES (?, ?, ?, ?) 
''', multiple_student_subjects) 
conn.commit() 
# Fetch all records 
cursor.execute('SELECT * FROM multiple_student_subjects') 
rows = cursor.fetchall() 
print("All Student Subjects Records:") 
for row in rows: 
    print(row) 
# Subjects with Marks > 90 
cursor.execute('SELECT name, Subject, Mark FROM multiple_student_subjects WHERE Mark > 90') 
high_marks = cursor.fetchall() 
print("\nSubjects with Marks greater than 90:") 
for subject in high_marks: 
    print(subject) 
# Update Mark for COA 
cursor.execute(''' 
UPDATE multiple_student_subjects  
SET Mark = 98  
WHERE Enrollment = 92400133161 AND Subject = 'ICE' 
''') 
conn.commit()
# Verify the update 
cursor.execute('''  
SELECT Subject, Mark FROM multiple_student_subjects  
WHERE Enrollment = 92400133161 AND Subject = 'ICE' 
''') 
updated = cursor.fetchone() 
print(f"\nUpdated Mark for ICE: {updated[1]}") 
# Delete marks for 'SS' subject 
cursor.execute(''' 
DELETE FROM multiple_student_subjects  
WHERE Enrollment = 92400133161 AND Subject = 'DMGT' 
''') 
conn.commit() 
# Verify deletion 
cursor.execute(''' 
SELECT * FROM multiple_student_subjects  
WHERE Enrollment = 92400133161 AND Subject = 'DMGT' 
''') 
deleted = cursor.fetchone() 
if deleted is None: 
    print("\n'DMGT' subject record has been successfully deleted") 
# Calculate the average Mark 
cursor.execute('''SELECT AVG(Mark) FROM multiple_student_subjects''') 
avg_mark = cursor.fetchone()[0] 
print(f"\nThe average mark of students is: {avg_mark:.2f}") 





