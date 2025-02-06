# Use to Connect the Data 
import psycopg2 
def table():
    # Taking the dbname , user , password , host from the psql
    conn = psycopg2.connect(dbname = "postgres" , user = "postgres" , password = "Usha1975@" , host  = "localhost" , port = "5432")

    # TO CREATE THE TABLE 
    # Make a variable cursor and execute the command in it .
    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text , ID int , Age int);''')
    print("Table created sucessfully")

    conn.commit()
    conn.close()

# INSERT THE DATE 
def data():
    # Taking the dbname , user , password , host from the psql
    conn = psycopg2.connect(dbname = "postgres" , user = "postgres" , password = "Usha1975@" , host  = "localhost" , port = "5432")

    
    # Make a variable cursor and execute the command in it .
    cursor = conn.cursor()

    Name = input('Enter the Name : ')
    ID = input("Enter the ID: ")
    Age = input("Enter the Age: ")

    query = '''insert into employees(Name, ID , Age) values(%s,%s,%s);'''
    cursor.execute(query,(Name,ID,Age))
    
    print("Data Added sucessfully")

    conn.commit()
    conn.close()

data()