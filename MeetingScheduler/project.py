import psycopg2
import tkinter as tk
import tkinter.font as tkFont

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

def logare(root):
    fereastra_logare = tk.Toplevel(root)
    fereastra_logare.title("Fereastra de Logare")
    fereastra_logare.geometry("600x600")
    fereastra_logare.configure(bg="#fef5e7")
    default_font = tkFont.Font(family="Bookman Old Style", size=12)
    root.option_add("*Font", default_font)

    main_frame = tk.Frame(fereastra_logare, bg="#fef5e7")
    main_frame.pack(expand=True, fill='both') 
    main_frame.place(relx=0.5, rely=0.5, anchor='center')

    label_logare = tk.Label(main_frame, text="Introduceti datele personale:", 
                            font=("Bookman Old Style", 16), bg="#fef5e7")
    label_logare.pack(pady=20)

    label_prenume = tk.Label(main_frame, text="Prenume:", bg="#fef5e7",
                             anchor='center', justify='center')
    label_prenume.pack(pady=5)
    entry_prenume = tk.Entry(main_frame, width=30, justify='center')
    entry_prenume.pack(pady=5)

    label_nume = tk.Label(main_frame, text="Nume:", bg="#fef5e7",
                          anchor='center', justify='center')
    label_nume.pack(pady=5)
    entry_nume = tk.Entry(main_frame, width=30, justify='center')
    entry_nume.pack(pady=5)

    label_email = tk.Label(main_frame, text="Email:", bg="#fef5e7", 
                           anchor='center', justify='center')
    label_email.pack(pady=5)
    entry_email = tk.Entry(main_frame, width=30, justify='center')
    entry_email.pack(pady=5)

    button_logare_secundar = tk.Button(main_frame, text="Logare", width=20)
    button_logare_secundar.pack(pady=10)
    button_logare_secundar.configure(bg="#f6ddcc")


def inserare_informatii(root):
    fereastra_inserare = tk.Toplevel(root)
    fereastra_inserare.title("Inserare Informatii")
    fereastra_inserare.geometry("600x600")
    fereastra_inserare.configure(bg="#fef5e7") 
    default_font = tkFont.Font(family="Bookman Old Style", size=12)
    root.option_add("*Font", default_font)

    main_frame = tk.Frame(fereastra_inserare, bg="#fef5e7")
    main_frame.place(relx=0.5, rely=0.5, anchor='center')

    label_informatii = tk.Label(main_frame, text="Alege actiunea dorita:", 
                                font=("Bookman Old Style", 18), bg="#fef5e7")
    label_informatii.pack(pady=20)

    button_adauga_persoana = tk.Button(main_frame, text="Adauga persoana",
                                       bg="#f6ddcc", width=20)
    button_adauga_persoana.pack(pady=10)

    button_stabileste_sedinta = tk.Button(main_frame,
                        text="Stabileste o sedinta", bg="#f6ddcc", width=20)
    button_stabileste_sedinta.pack(pady=10)

    button_vezi_sedinte = tk.Button(main_frame, text="Vezi sedintele", 
                                    bg="#f6ddcc", width=20)
    button_vezi_sedinte.pack(pady=10)

def creeaza_interfata():
    root = tk.Tk()
    root.title("Meeting Scheduler")
    root.geometry("600x600") 
    root.configure(bg="#fef5e7")
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True)
    main_frame.configure(bg="#fef5e7")

    label = tk.Label(main_frame, text="Meeting Scheduler", 
                     font=("Bookman Old Style", 16))
    label.pack(pady=20)
    label.configure(bg="#fef5e7")

    button_logare = tk.Button(main_frame, text="Logare", 
                              font=("Bookman Old Style", 12), width=20, 
                              command=lambda: logare(root))
    button_logare.pack(pady=10)
    button_logare.configure(bg="#f6ddcc")

    button_inserare = tk.Button(main_frame, text="Inserare informatii", 
                                font=("Bookman Old Style", 12), width=20, 
                                command=lambda: inserare_informatii(root))
    button_inserare.pack(pady=10)
    button_inserare.configure(bg="#f6ddcc")

    root.mainloop()

creeaza_interfata()
