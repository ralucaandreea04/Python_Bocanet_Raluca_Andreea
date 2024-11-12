import os
import sys
#EXERCITIUL 1

def problem1():
    try:
        if len(sys.argv) != 4:
            raise ValueError("nu sunt suficiente argumente")

        directory = sys.argv[1]
        extension = sys.argv[2]

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"nu exista directorul {directory}")

        if not extension.startswith("."):
            raise ValueError("extensie invalida")

        for filename in os.listdir(directory):
            if filename.endswith(extension):
                file_path = os.path.join(directory, filename)
                try:
                    with open(file_path, 'r') as file:
                        print(f"Fisierul {filename} contine:")
                        print(file.read())
                        print("=" * 60)
                except FileNotFoundError:
                    print(f"fisier nu a fost gasit: {filename}")
                except Exception as e:
                    print(f"eroare la citirea fisierului {filename}: {e}")
    except Exception as e:
        print(f"Eroare: {e}")

problem1()

#EXERCITIUL 2
def problem2(directory):
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"nu exista directorul {directory}")
        
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        for index, filename in enumerate(files, start=1):
            file_path = os.path.join(directory, filename)
            new_name = f"file{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_name)
            try:
                os.rename(file_path, new_path)
                print(f"Fisirul {filename} a fost redenumit in {new_name}")
            except Exception as e:
                print(f"Eroare la citire: {e}")
    except NotADirectoryError as nde:
        print(nde)
    except Exception as e:
        print(f"Eroare: {e}")

problem2("C:/Users/raluc/OneDrive/Desktop/teste")
print("=" * 60)

#EXERCITIUL 3
def problem3():
    if len(sys.argv) != 4:
            raise ValueError("nu sunt suficiente argumente")
    directory = sys.argv[3]
    total_size = 0
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"nu exista directorul {directory}")
        
        for root, _, files in os.walk(directory): 
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except Exception as e:
                    print(f"Nu am putut accesa fisierul: {e}")
        
        print(f"Size : {total_size} ")
    except NotADirectoryError as nde:
        print(nde)
    except Exception as e:
        print(f"Eroare: {e}")

problem3()
print("=" * 60)

#EXERCITIUL 4
def problem4():
    if len(sys.argv) != 4:
            raise ValueError("nu sunt suficiente argumente")
    directory = sys.argv[3]
    extension_count = {}
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"nu exista directorul {directory}")
        
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                extension = os.path.splitext(filename)[1]
                
                if extension in extension_count:
                    extension_count[extension] += 1
                else:
                    extension_count[extension] = 1 
        
        if extension_count:
            print("Extensii:")
            for ext, count in extension_count.items():
                print(f"{ext}: {count}")
        else:
            print("Nu exista fisiere in director.")
    except NotADirectoryError as nde:
        print(nde)
    except Exception as e:
        print(f"Eroare: {e}")

problem4()