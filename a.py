______import mysql.connector
import json

conn = mysql.connector.connect(
    host='localhost',     
    user='root',      
    password='Jaga@123',  
    database='employee_db'    
)


cursor = conn.cursor()


create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        employeeId INT NOT NULL,
        firstName VARCHAR(255) NOT NULL,
        lastName VARCHAR(255) NOT NULL
    )
'''
cursor.execute(create_table_query)

try:
    with open("profile_details.json") as f:
    data = json.load(f)

    insert_query = '''
        INSERT INTO users (employeeId, firstName, lastName) VALUES (%s, %s, %s)
    '''

    for i in data['emp_details']:
        employeeId = i['employeeId']
        firstName = i['firstName']
        lastName = i['lastName']
        data_to_insert = (employeeId, firstName, lastName)
        cursor.execute(insert_query, data_to_insert)
        conn.commit()
        
    f.close()


    cursor.close()
    conn.close()