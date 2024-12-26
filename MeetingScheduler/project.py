import psycopg2

def conectare_baza_de_date():
    try:
        conn = psycopg2.connect(
            host="localhost", 
            database="meeting_db",  
            user="postgres", 
            password="1234Raluca" 
        )
        return conn
    except psycopg2.Error as e:
        print(f"eroare la conectarea bazei de date: {e}")

def executare_sql_script(file_path):
    try:
        conn = conectare_baza_de_date()
        cursor = conn.cursor()

        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()

        cursor.execute(sql_script)
        conn.commit()

        print(f"s-a executat cu succes scriptul '{file_path}'")

    except psycopg2.Error as e:
        print(f"eroare la executare: {e}")

def adaugare_participant(nume, prenume, email):
    try:
        conn = conectare_baza_de_date()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO people (first_name, last_name, email) 
            VALUES (%s, %s, %s)
            """, 
            (nume, prenume, email)
        )
        conn.commit()

    except psycopg2.Error as e:
        print(f"eroare la adaugare: {e}")

def afisare_participanti():
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM people")
    print(cursor.fetchall())

def adaugare_sedinta(data_inceput, data_sfarsit,descriere,lista_participanti):
    try:
        conn = conectare_baza_de_date()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO meetings (start_time, end_time, description) 
            VALUES (%s, %s, %s) RETURNING id
            """, 
            (data_inceput, data_sfarsit, descriere)
        )
        sedinta_id = cursor.fetchone()[0]

        for participant_id in lista_participanti:
            cursor.execute(
                """
                INSERT INTO meeting_participants (meeting_id, person_id) 
                VALUES (%s, %s)"
                """, 
                (sedinta_id, participant_id)
            )

        conn.commit()

    except psycopg2.Error as e:
        print(f"eroare la adaugare: {e}")

def afisare_sedinte():
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meetings")
    print("Sedintele sunt:")
    print(cursor.fetchall())

def afisare_participanti_sedinta(sedinta_id):
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT p.first_name, p.last_name, p.email
        FROM people p
        JOIN meeting_participants mp
        ON p.id = mp.person_id
        WHERE mp.meeting_id = %s
        """,
        (sedinta_id,)
    )
    print(f"Participanti pentru sedinta {sedinta_id}:")
    print(cursor.fetchall())

def afisarea_sedintelor_timp(data_inceput, data_sfarsit):
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM meetings WHERE start_time >= %s AND end_time <= %s", 
        (data_inceput, data_sfarsit)
    )
    print("Sedintele sunt:")
    print(cursor.fetchall())

def main():
    print("Persoanele sunt:")
    afisare_participanti()
    afisare_sedinte()
    afisare_participanti_sedinta(2)

main()