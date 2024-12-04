import mysql.connector
import pandas as pd

try:
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='nandu15',
        database='nandu'
    )
    if conn.is_connected():
        print('connected successfully')

    cursor=conn.cursor()
    query = "SELECT * FROM Employee;"

    # query='insert into Employee(eid,efirst_name,elast_name,ephne_no,ework_location) values(%s,%s,%s,%s,%s)'
    # data=[('12345','Bodagala','Nandini',103,"Bangalore"),('56345757','Maramsetty',"Kavya",2056,"Chennai"),('5859348','kandula','Sridevi',1043,"Hyderabad")]

    # cursor.executemany(query,data)
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    conn.commit()

    print(f"{cursor.rowcount} record inserted, ID: {cursor.lastrowid}")

    df = pd.DataFrame(result, columns=columns)
    df.to_excel("employee_data_mysql.xlsx", index=False)
    print("Data saved to Excel successfully!")


except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
       cursor.close()
       conn.close()
       print("MySQL connection is closed.")