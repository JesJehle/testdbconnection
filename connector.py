import psycopg2

try:
    connection = psycopg2.connect(
        user='janusch',
        password='backup2',
        host='localhost',
        database='pgtutor'
    )
    cursor = connection.cursor()

    print(connection.get_dsn_parameters())
    # Print PostgreSQL version
    cursor.execute("SELECT name, address, state FROM purchases;")
    record = cursor.fetchmany()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
