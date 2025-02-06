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


def data():
    # Taking the dbname , user , password , host from the psql
    conn = psycopg2.connect(dbname = "postgres" , user = "postgres" , password = "Usha1975@" , host  = "localhost" , port = "5432")

    # TO INSERT VALUE IN THE TABLE 
    # Make a variable cursor and execute the command in it .
    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name, ID , Age) values('Sam' , 01,30);''')
    print("Data Added sucessfully")

    conn.commit()
    conn.close()



def extract():
    # Taking the dbname , user , password , host from the psql
    conn = psycopg2.connect(dbname = "postgres" , user = "postgres" , password = "Usha1975@" , host  = "localhost" , port = "5432")

    # TO INSERT VALUE IN THE TABLE 
    # Make a variable cursor and execute the command in it .
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show = print(cursor.fetchone())
    print(show)

    conn.commit()
    conn.close()

extract()
