import psycopg2

def conectare_baza_de_date():
    try:
        connection = psycopg2.connect(
            host="localhost", 
            database="meeting_db",  
            user="postgres", 
            password="1234Raluca" 
        )
        print("conectare reusita")
        return connection
    except psycopg2.Error as e:
        print(f"eroare la conectarea bazei de date: {e}")
        return None

def executare_sql_script(file_path):
    try:
        connection = conectare_baza_de_date()
        cursor = connection.cursor()

        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()

        cursor.execute(sql_script)
        connection.commit()

        print(f"s-a executat cu succes scriptul '{file_path}'")

    except psycopg2.Error as e:
        print(f"eroare la executare: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

executare_sql_script("MeetingScheduler/create_tables.sql")