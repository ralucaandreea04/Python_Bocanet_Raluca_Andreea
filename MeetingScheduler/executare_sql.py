import psycopg2
import project as p

def executare_sql_script(file_path):
    """
    Functia de executare a unui script SQL
    :param file_path: calea catre fisierul SQL
    :type file_path: string
    """
    try:
        conn = p.conectare_baza_de_date()
        cursor = conn.cursor()

        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()

        cursor.execute(sql_script)
        conn.commit()

        print(f"s-a executat cu succes scriptul '{file_path}'")

    except psycopg2.Error as e:
        print(f"eroare la executare: {e}")