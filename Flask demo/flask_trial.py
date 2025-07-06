import sqlite3

# Connect to DB. For this to work, sqlite.db must be in the same folder as your .py file!
conn = sqlite3.connect('sqlite.db')

# Create a cursor object - required for running queries on the DB
cursor = conn.cursor()

# Create the subjects table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    subjectid INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    exam_board TEXT,
    course_code TEXT,
    email TEXT
)
""")
conn.commit()

# Insert sample entries into the subjects table (can be reused for testing)
def addSubjects(email):
    subject = ""
    examboard = ""
    course = ""
    while subject == "" and examboard == "" and course == "":
        subject = input("Enter the name of the subject: ")
        examboard = input("Enter the examboard: ")
        course = input("Enter the course code: ")
    try:
        cursor.executemany("""
        INSERT INTO subjects (subject_name, exam_board, course_code, email) 
        VALUES (?, ?, ?, ?)
        """, [
            (subject, examboard, course, email)
        ])
        conn.commit()
        print("Subjects added.")
    except Exception as e:
        print("Error adding subjects:", e)
        conn.rollback()

# Allow the user to view their subjects after logging in
def viewSubjects(email):
    try:
        cursor.execute("""
        SELECT subject_name, exam_board, course_code 
        FROM subjects 
        WHERE email = ?
        """, (email,))
        subjects = cursor.fetchall()
        if subjects:
            print("Subjects associated with your account:")
            for subject in subjects:
                print(f"Subject: {subject[0]}, Exam Board: {subject[1]}, Course Code: {subject[2]}")
        else:
            print("No subjects found for your account.")
    except Exception as e:
        print("Error fetching subjects:", e)

def deleteSubjects(email):
    subject = ""
    while subject == "":
        subject = input("Enter the subject you want to delete: ")
    try:
        cursor.execute("DELETE FROM subjects WHERE email = '"+email+"' AND subject_name = '"+subject+"'")
        conn.commit()
        print(subject,"deleted.")
    except Exception as e:
        print("Error finding subject:",e)

# Whether user wants to input again
def runAgain():
    choice = ""
    while choice != "y" and choice != "n":
        choice = input("Would you like to run the program? (y/n)")
    if choice == "y":
        return True
    elif choice == "n":
        return False

# What does the user wants to do
def userChoice():
    choice = ""
    while choice != "1" and choice != "2" and choice != "3" and choice!= "4":
        print("What would you like to do? Choose a number.")
        print("1. Create a new account")
        print("2. Log in to your account")
        print("3. Display all values")
        print("4. Delete all values")
        choice = input("Enter your choice: ")
    if choice == "1":
        createAcc()
    elif choice == "2":
        loginAcc()
    elif choice == "3":
        displayAll()
    elif choice == "4":
        deleteAll()

# Print all values
def displayAll():
    cursor.execute("SELECT * FROM accounts")
    records = cursor.fetchall()
    for row in records:
        print(row)

# Password hash method
def passHash(password):
    hash=0
    for ch in password:
        hash = ( hash*281  ^ ord(ch)*997) & 0xFFFFFFFF
    return str(hash)

    # listPassword = []
    # for i in range(len(password)):
    #     listPassword.append(chr(ord(password[i])+1))
    # hashPassword = ''.join(listPassword)
    # return hashPassword

# Reverse password hash method
    
    # listPassword = []
    # for i in range(len(hashPassword)):
    #     listPassword.append(chr(ord(hashPassword[i])-1))
    # password = ''.join(listPassword)
    # return password 

# Allow for account creation 
def createAcc():
    email = ""
    while email == "":
        email = input("Enter your email: ")
    password = ""
    while password == "":
        password = input("Enter your password: ")

    cursor.execute("SELECT * FROM accounts WHERE email = '" + email + "'")
    records = cursor.fetchall()
    if len(records) == 0:
        var = f" '{email}', '{passHash(password)}'"
        query = f"INSERT INTO accounts(email, password) VALUES ({var})"
        cursor.execute(query)
        conn.commit()
        print("New account created for:",email)
    else:
        print("Email already registered with an account, please try again.")

def loginAcc():
    # Test login. First, get email and password input from user
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    # Run query to get any records with that email and password combination
    cursor.execute("SELECT * FROM accounts WHERE email = '" + email + "' AND password = '" + passHash(password) + "'")
    records = cursor.fetchall() # technically, only one record should be returned...
    if len(records) == 0:
        print("Invalid username or password")
    else:
        print("Login successful. You have successfully logged in for",email)
        choice = "n"
        while choice == "n":
            print("Options:")
            print("1. View your subjects")
            print("2. Add subjects")
            print("3. Delete subjects")
            choice = ""
            while choice == "":
                choice = input("Enter your choice: ")
            if choice == "1":
                viewSubjects(email)
            elif choice == "2":
                addSubjects(email)
            elif choice == "3":
                deleteSubjects(email)
            choice = ""
            while choice != "y" and choice != "n":
                choice = input("Do you wanna log out? (y/n)")

def deleteAll():
    try:
        cursor.execute("DELETE FROM accounts")
        conn.commit()
        print("Deleted all values!")
    except:
        conn.rollback()

# Main code
while runAgain(): 
    userChoice()
print("Thanks for using the program!!")

# Close the connection
conn.close()
exit()