import psycopg2
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
from ics import Calendar

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

def adauga(root):
    fereastra_adauga = tk.Toplevel(root)
    fereastra_adauga.title("Fereastra de Adaugare Persoana")
    fereastra_adauga.geometry("600x600")
    fereastra_adauga.configure(bg="#fef5e7")
    default_font = tkFont.Font(family="Bookman Old Style", size=12)
    root.option_add("*Font", default_font)

    main_frame = tk.Frame(fereastra_adauga, bg="#fef5e7")
    main_frame.pack(expand=True, fill='both') 
    main_frame.place(relx=0.5, rely=0.5, anchor='center')

    label_adaugare = tk.Label(main_frame, text="Introduceti datele:", 
                            font=("Bookman Old Style", 16), bg="#fef5e7")
    label_adaugare.pack(pady=20)

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

    button_adaugare = tk.Button(main_frame, text="Adaugare", width=20,
                                       command=lambda:adaugare_participant(
                                           entry_prenume.get(),
                                           entry_nume.get(),
                                           entry_email.get()
                                        )
                                       )
    button_adaugare.pack(pady=10)
    button_adaugare.configure(bg="#f6ddcc")

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
        if cursor.rowcount > 0:
             messagebox.showinfo("Succes",
                f"Participantul a fost adaugat cu succes!")
        else:
            messagebox.showerror("Eroare", "Participantul nu a fost adaugat!")
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

        for participant in lista_participanti.split(","):
            participant_prenume, participant_nume = participant.strip().split()
            cursor.execute(
                """
                SELECT id FROM people
                WHERE first_name = %s AND last_name = %s
                """,
                (participant_prenume, participant_nume)
            )

            participant_id = cursor.fetchone()
            if participant_id:
                participant_id = participant_id[0]
                cursor.execute(
                    """
                    INSERT INTO meeting_participants (meeting_id, person_id)
                    VALUES (%s, %s)
                    """,
                    (sedinta_id, participant_id)
                )
            else:
                messagebox.showerror(
                    "Eroare", 
                    f"Participantul {participant} nu exista!"
                    )
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Succes","Sedinta a fost adaugata cu succes!")
        else:
            messagebox.showerror("Eroare", "Sedinta nu a fost adaugata!")

    except psycopg2.Error as e:
        print(f"eroare la adaugare: {e}")

def inserare_sedinta(root):
    fereastra_inserare = tk.Toplevel(root)
    fereastra_inserare.title("Fereastra de Adaugare Sedinta")
    fereastra_inserare.geometry("600x600")
    fereastra_inserare.configure(bg="#fef5e7")
    default_font = tkFont.Font(family="Bookman Old Style", size=12)
    root.option_add("*Font", default_font)

    main_frame = tk.Frame(fereastra_inserare, bg="#fef5e7")
    main_frame.pack(expand=True, fill='both') 
    main_frame.place(relx=0.5, rely=0.5, anchor='center')

    label_sedinta = tk.Label(main_frame, text="Introduceti datele:", 
                            font=("Bookman Old Style", 16), bg="#fef5e7")
    label_sedinta.pack(pady=20)

    label_descriere = tk.Label(main_frame, text="Descriere:", bg="#fef5e7",
                             anchor='center', justify='center')
    label_descriere.pack(pady=5)
    entry_descriere = tk.Entry(main_frame, width=30, justify='center')
    entry_descriere.pack(pady=5)

    label_data_ora_inceput= tk.Label(main_frame, 
                                     text="Data si ora de inceput:", 
                                     bg="#fef5e7",
                                     anchor='center', 
                                     justify='center'
                                    )
    label_data_ora_inceput.pack(pady=5)
    entry_data_ora_inceput = tk.Entry(main_frame, width=30, justify='center')
    entry_data_ora_inceput.pack(pady=5)

    label_data_ora_sfarsit= tk.Label(main_frame, 
                                     text="Data si ora de incheiere:", 
                                     bg="#fef5e7",
                                     anchor='center', 
                                     justify='center'
                                    )
    label_data_ora_sfarsit.pack(pady=5)
    entry_data_ora_sfarsit = tk.Entry(main_frame, width=30, justify='center')
    entry_data_ora_sfarsit.pack(pady=5)

    label_participanti = tk.Label(main_frame, 
                                  text="Participanti:", 
                                  bg="#fef5e7",
                                  anchor='center', 
                                  justify='center'
                                )
    label_participanti.pack(pady=5)
    entry_participanti = tk.Entry(main_frame, width=30, justify='center')
    entry_participanti.pack(pady=5)

    button_adaugare = tk.Button(
                                main_frame, 
                                text="Adaugare", 
                                width=20,
                                command=lambda:adaugare_sedinta(
                                    entry_data_ora_inceput.get(),
                                    entry_data_ora_sfarsit.get(),
                                    entry_descriere.get(),
                                    entry_participanti.get()
                                )
                            )
    button_adaugare.pack(pady=10)
    button_adaugare.configure(bg="#f6ddcc")


def afisare_sedinte(prenume, nume, email):
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT m.id, m.start_time, m.end_time, m.description
        FROM meetings m
        JOIN meeting_participants mp
        ON m.id = mp.meeting_id
        JOIN people p
        ON p.id = mp.person_id
        WHERE p.first_name = %s AND p.last_name = %s AND p.email = %s
        """,
        (prenume, nume, email)
    )
    return cursor.fetchall()

def afisare_participanti_sedinta(sedinta_id):
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT p.first_name, p.last_name
        FROM people p
        JOIN meeting_participants mp
        ON p.id = mp.person_id
        WHERE mp.meeting_id = %s
        """,
        (sedinta_id,)
    )
    participanti = cursor.fetchall()
    lista= []
    for participant in participanti:
        lista.append(f"{participant[0]} {participant[1]}")
    return ", ".join(lista)

def afisarea_sedintelor_timp(data_inceput, data_sfarsit):
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM meetings WHERE start_time >= %s AND end_time <= %s", 
        (data_inceput, data_sfarsit)
    )
    print("Sedintele sunt:")
    print(cursor.fetchall())

def test_credentiale_logare(prenume, nume, email):
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM people
        WHERE first_name = %s AND last_name = %s AND email = %s
        """,
        (prenume, nume, email)
    )
    rezultat = cursor.fetchall()
    if len(rezultat) > 0:
        participant_logat(prenume, nume, email)
    return "Datele introduse nu sunt corecte!"

def participant_logat(prenume, nume, email):
    fereastra = tk.Toplevel()
    fereastra.title(f"Meeting Scheduler - {prenume} {nume}")
    fereastra.geometry("600x600")
    fereastra.configure(bg="#fef5e7")

    label_bun_venit = tk.Label(
        fereastra, 
        text=f"Bun venit, {prenume}!", 
        font=("Bookman Old Style", 16), 
        bg="#fef5e7"
    )
    label_bun_venit.pack(pady=20)

    label_sedinte = tk.Label(
        fereastra, 
        text="Sedintele tale programate:", 
        font=("Bookman Old Style", 13), 
        bg="#fef5e7",
    )
    label_sedinte.pack(pady=10)

    frame_tabel = tk.Frame(fereastra, bg="#fef5e7")
    frame_tabel.pack(pady=10)

    style = ttk.Style()
    style.configure(
        "mystyle.Treeview", 
        font=("Bookman Old Style", 8),
        rowheight=30, 
        background="#fef5e7",
        fieldbackground="#fef5e7" 
    )
    style.configure(
        "mystyle.Treeview.Heading", 
        font=("Bookman Old Style", 14, "bold"), 
        background="#f6ddcc", 
        foreground="#4a4a4a"
    )

    tabel = ttk.Treeview(
            frame_tabel, 
            columns=("Interval", "Descriere"), 
            show="headings", 
            height=5,
            style="mystyle.Treeview"
            )
    tabel.heading("Interval", text="Interval")
    tabel.heading("Descriere", text="Descriere")
    tabel.column("Interval", anchor="center", width=275)
    tabel.column("Descriere", anchor="center", width=275)
    tabel.pack(pady=10)

    lista_sedinte = afisare_sedinte(prenume, nume, email)
    if lista_sedinte:
        for sedinta in lista_sedinte:
            interval = f"{sedinta[1]} - {sedinta[2]}"
            tabel.insert("", "end", values=(interval, sedinta[3]))
    else:
        tabel.insert("", "end", values=("Nu sunt sedinte", "", ""))

    button_inchide = tk.Button(
        fereastra, 
        text="Inchide", 
        command=fereastra.destroy, 
        bg="#f6ddcc", 
        width=20
    )
    button_inchide.pack(pady=20)

def afisare_orar(data_inceput, data_sfarsit):
    conn=conectare_baza_de_date()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM meetings WHERE start_time >= %s AND end_time <= %s", 
        (data_inceput, data_sfarsit)
    )
    return cursor.fetchall()

def afisare_sedinte_orar(data_inceput, data_sfarsit):
    fereastra = tk.Toplevel()
    fereastra.title(f"Meeting Scheduler - {data_inceput} - {data_sfarsit}")
    fereastra.geometry("850x600")
    fereastra.configure(bg="#fef5e7")

    label_sedinte = tk.Label(
        fereastra, 
        text="Sedintele programate sunt:", 
        font=("Bookman Old Style", 13), 
        bg="#fef5e7",
    )
    label_sedinte.pack(pady=10)

    frame_tabel = tk.Frame(fereastra, bg="#fef5e7")
    frame_tabel.pack(pady=10)

    style = ttk.Style()
    style.configure(
        "mystyle.Treeview", 
        font=("Bookman Old Style", 9),
        rowheight=40, 
        background="#fef5e7",
        fieldbackground="#fef5e7" 
    )
    style.configure(
        "mystyle.Treeview.Heading", 
        font=("Bookman Old Style", 14, "bold"), 
        background="#f6ddcc", 
        foreground="#4a4a4a"
    )

    tabel = ttk.Treeview(
            frame_tabel, 
            columns=("Interval", "Descriere","Participanti"), 
            show="headings", 
            height=5,
            style="mystyle.Treeview"
            )
    tabel.heading("Interval", text="Interval")
    tabel.heading("Descriere", text="Descriere")
    tabel.heading("Participanti", text="Participanti")
    tabel.column("Interval", anchor="center", width=275)
    tabel.column("Descriere", anchor="center", width=275)
    tabel.column("Participanti", anchor="center", width=275)
    tabel.pack(pady=10)

    lista_sedinte = afisare_orar(data_inceput, data_sfarsit)
    if lista_sedinte:
        for sedinta in lista_sedinte:
            interval = f"{sedinta[1]} - {sedinta[2]}"
            participanti = afisare_participanti_sedinta(sedinta[0])
            tabel.insert("", "end", 
                         values=(interval, sedinta[3], participanti)
                        )

    button_inchide = tk.Button(
        fereastra, 
        text="Inchide", 
        command=fereastra.destroy, 
        bg="#f6ddcc", 
        width=20
    )
    button_inchide.pack(pady=20)

def date_sedinte(root):
    fereastra_sedinte = tk.Toplevel(root)
    fereastra_sedinte.title("Date Sedinte")
    fereastra_sedinte.geometry("600x600")
    fereastra_sedinte.configure(bg="#fef5e7")
    default_font = tkFont.Font(family="Bookman Old Style", size=12)
    root.option_add("*Font", default_font)

    main_frame = tk.Frame(fereastra_sedinte, bg="#fef5e7")
    main_frame.pack(expand=True, fill='both') 
    main_frame.place(relx=0.5, rely=0.5, anchor='center')

    label_sedinte = tk.Label(main_frame, text="Introduceti orele dorite:", 
                            font=("Bookman Old Style", 16), bg="#fef5e7")
    label_sedinte.pack(pady=20)

    label_inceput = tk.Label(main_frame, text="Data la care a inceput:", 
                             bg="#fef5e7", anchor='center', justify='center')
    label_inceput.pack(pady=5)
    entry_inceput = tk.Entry(main_frame, width=30, justify='center')
    entry_inceput.pack(pady=5)

    label_sfarsit = tk.Label(main_frame, text="Data la care s-a terminat:", 
                          bg="#fef5e7", anchor='center', justify='center')
    label_sfarsit.pack(pady=5)
    entry_sfarsit = tk.Entry(main_frame, width=30, justify='center')
    entry_sfarsit.pack(pady=5)

    button_sedinte = tk.Button(main_frame, 
                                       text="Vizualizare", 
                                       width=20,
                                       command=lambda: afisare_sedinte_orar(
                                        entry_inceput.get(),
                                        entry_sfarsit.get(),
                                        )
                                    )   
    button_sedinte.pack(pady=10)
    button_sedinte.configure(bg="#f6ddcc")

def export_calendar_nume(nume):
        prenume, nume = nume.split()
        conn = conectare_baza_de_date()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT m.start_time, m.end_time, m.description
            FROM meetings m
            JOIN meeting_participants mp ON m.id = mp.meeting_id
            JOIN people p ON p.id = mp.person_id
            WHERE p.first_name = %s AND p.last_name = %s
            """,
            (prenume, nume)
        )
        sedinte = cursor.fetchall()

        filename = f"{prenume}_{nume}_calendar.ics"
        with open(filename, "w") as f:
            f.write("BEGIN:VCALENDAR\n")
            f.write("PRODID:-//Meeting Scheduler//EN\n")
            for sedinta in sedinte:
                f.write("BEGIN:VEVENT\n")
                f.write(f"DTSTART:{sedinta[0].strftime('%Y%m%dT%H%M%S')}\n")
                f.write(f"DTEND:{sedinta[1].strftime('%Y%m%dT%H%M%S')}\n")
                f.write(f"SUMMARY:{sedinta[2]}\n")
                f.write("END:VEVENT\n")
            f.write("END:VCALENDAR\n")

def export_calendar_data(start_date, end_date):
        conn = conectare_baza_de_date()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT start_time, end_time, description
            FROM meetings
            WHERE start_time >= %s AND end_time <= %s
            """,
            (start_date, end_date)
        )
        sedinte = cursor.fetchall()

        filename = f"calendar_data.ics"
        with open(filename, "w") as f:
            f.write("BEGIN:VCALENDAR\n")
            f.write("PRODID:-//Meeting Scheduler//EN\n")
            for sedinta in sedinte:
                f.write("BEGIN:VEVENT\n")
                f.write(f"DTSTART:{sedinta[0].strftime('%Y%m%dT%H%M%S')}\n")
                f.write(f"DTEND:{sedinta[1].strftime('%Y%m%dT%H%M%S')}\n")
                f.write(f"SUMMARY:{sedinta[2]}\n")
                f.write("END:VEVENT\n")
            f.write("END:VCALENDAR\n")

def export_sedinte():
        conn = conectare_baza_de_date()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT start_time, end_time, description
            FROM meetings
            """
        )
        sedinte = cursor.fetchall()

        filename = "sedinte.ics"
        with open(filename, "w") as f:
            f.write("BEGIN:VCALENDAR\n")
            f.write("PRODID:-//Meeting Scheduler//EN\n")
            for sedinta in sedinte:
                f.write("BEGIN:VEVENT\n")
                f.write(f"DTSTART:{sedinta[0].strftime('%Y%m%dT%H%M%S')}\n")
                f.write(f"DTEND:{sedinta[1].strftime('%Y%m%dT%H%M%S')}\n")
                f.write(f"SUMMARY:{sedinta[2]}\n")
                f.write("END:VEVENT\n")
            f.write("END:VCALENDAR\n")

def import_calendar(fisier):
    conn = conectare_baza_de_date()
    cursor = conn.cursor()

    with open(fisier, 'r') as f:
        calendar = Calendar(f.read())

    for event in calendar.events:
        start_time = event.begin.datetime.strftime("%Y-%m-%d %H:%M:%S")
        end_time = event.end.datetime.strftime("%Y-%m-%d %H:%M:%S")
        description = event.name

        cursor.execute(
            """
            INSERT INTO meetings (start_time, end_time, description)
            VALUES (%s, %s, %s)
            """,
            (start_time, end_time, description)
        )
    conn.commit()
    conn.close()

def import_export_calendar(root):
    fereastra = tk.Toplevel(root)
    fereastra.title("Import / Export Calendar")
    fereastra.geometry("800x600")
    fereastra.configure(bg="#fef5e7")

    main_frame = tk.Frame(fereastra, bg="#fef5e7")
    main_frame.pack(fill="both", expand=True)

    frame_export = tk.Frame(main_frame, bg="#e8f6f3", padx=20, pady=20, 
                            relief="groove", borderwidth=2)
    frame_export.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    frame_import = tk.Frame(main_frame, bg="#fcf3cf", padx=20, pady=20, 
                            relief="groove", borderwidth=2)
    frame_import.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)

    tk.Label(frame_export, text="Export", 
             font=("Bookman Old Style", 16, "bold"), 
             bg="#e8f6f3").pack(pady=10)

    tk.Label(frame_export, text="Numele persoanei:", 
             bg="#e8f6f3").pack(anchor="w", pady=5)
    entry_name = tk.Entry(frame_export, width=40)
    entry_name.pack(pady=5)
    tk.Button(frame_export, text="Export dupa persoana", bg="#d5f5e3",
              command=lambda: export_calendar_nume(
                  entry_name.get()
                  )
                ).pack(pady=10)

    tk.Label(frame_export, text="Interval de date (YYYY-MM-DD):", 
             bg="#e8f6f3").pack(anchor="w", pady=5)
    entry_start_date = tk.Entry(frame_export, width=40)
    entry_start_date.pack(pady=5)
    entry_end_date = tk.Entry(frame_export, width=40)
    entry_end_date.pack(pady=5)
    tk.Button(frame_export, text="Export dupa interval", bg="#d5f5e3",
              command=lambda: export_calendar_data(
                  entry_start_date.get(), 
                  entry_end_date.get()
                  )
                ).pack(pady=10)

    tk.Label(frame_export, text="Toate sedintele:", 
             bg="#e8f6f3").pack(anchor="w", pady=5)
    tk.Button(frame_export, text="Export toate", bg="#d5f5e3", 
              command=export_sedinte).pack(pady=10)

    tk.Label(frame_import, text="Import", 
             font=("Bookman Old Style", 16, "bold"), 
             bg="#fcf3cf").pack(pady=10)
    tk.Label(frame_import, text="Introduceti datele pentru import:", 
             bg="#fcf3cf").pack(anchor="w", pady=5)
    entry_import = tk.Entry(frame_import, width=40)
    entry_import.pack(pady=10)
    tk.Button(frame_import, 
              text="Import", 
              bg="#fdebd0",
              command=lambda: import_calendar(entry_import.get())
                  ).pack(pady=20)


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

    button_logare_secundar = tk.Button(main_frame, text="Logare", width=20,
                                       command=lambda:test_credentiale_logare
                                       (
                                        entry_prenume.get(),entry_nume.get(),
                                        entry_email.get()
                                        )
                                       )
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
                                       bg="#f6ddcc", width=20, 
                                       command=lambda: adauga(root))
    button_adauga_persoana.pack(pady=10)

    button_stabileste_sedinta = tk.Button(main_frame,
                        text="Stabileste o sedinta", 
                        bg="#f6ddcc", 
                        width=20,
                        command=lambda: inserare_sedinta(root)
                        )
    button_stabileste_sedinta.pack(pady=10)

    button_import_export = tk.Button(main_frame,
                                    text="Import/Export calendar",
                                    bg="#f6ddcc", 
                                    width=20,
                                    command=lambda:import_export_calendar(root)
                                )
    button_import_export.pack(pady=10)

    button_vezi_sedinte = tk.Button(main_frame, 
                                    text="Vezi sedintele", 
                                    bg="#f6ddcc", 
                                    width=20,
                                    command=lambda: date_sedinte(root),
                                )
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
