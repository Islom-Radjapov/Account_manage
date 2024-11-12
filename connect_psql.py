import psycopg2

connection = psycopg2.connect(database="postgres", user="myuser", password="mypassword", host="185.195.26.133", port=5432)

cursor = connection.cursor()
print(cursor)
cursor.execute("SELECT * from portal.portal_users;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)
