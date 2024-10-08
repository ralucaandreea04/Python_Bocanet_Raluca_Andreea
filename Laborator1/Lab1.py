#EXERCIUTL 1
def cmmdc_2(a, b):
    a=int(a)
    b=int(b)
    while b:
        r=a%b
        a=b
        b=r
    return a

def problem_1(numere):
    rez = cmmdc_2(numere[0], numere[1])
    for i in range(2, len(numere)):
        rez = cmmdc_2(rez, numere[i])
    return rez

n = int(input("n = "))
numere = []
numere = list(map(int, input("numerele: ").split()))

cmmdc_rezultat = problem_1(numere)
print("CMMDDC-ul numerelor este :", cmmdc_rezultat)

#--------------------------------------------

#EXERCIUTL 2
def problem_2(sir):
    vocale = "aeiou"
    nr = 0
    for i in sir:
        if i in vocale:
            nr += 1
    return nr

cuvant = input("cuvant = ")
print("Numarul de vocale: ", problem_2(cuvant))

#--------------------------------------------

#EXERCIUTL 3
def problem_3(sir1, sir2):
    sir1=sir1.lower()
    sir2=sir2.lower()
    return sir2.count(sir1)

sir1 = input("Primul sir este: ")
sir2 = input("Al doilea sir este: ")
print("Numarul de aparitii ale sirului 1 in sirul 2 este: ", problem_3(sir1,sir2))

#--------------------------------------------


#EXERCIUTL 4
def problem_4(sir):
    sir_nou = ""
    index = 0
    for i in sir:
        if i.isupper():
            if index == 0:
                sir_nou += i.lower()
            else:
                sir_nou += "_" + i.lower()
        else:
            sir_nou += i
        index += 1
    return sir_nou

sir = input("sirul de caractere: ")
print(problem_4(sir))

#--------------------------------------------

#EXERCIUTL 5
def problem_5(numar):
    for i in range(len(numar)//2):
        if numar[i] != numar[len(numar)-1]:
            return False
    return True

numar = input("numar: ")
if problem_5(numar):
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")

#--------------------------------------------

#EXERCIUTL 6
def problem_6(text):
    number = ''
    for character in text:
        if character.isdigit():
            number += character
        elif number:
            break
    return number

text = input("text: ")
print(problem_6(text))

#--------------------------------------------

#EXERCIUTL 7
def number_binary(number):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary

def problem_7(nr_binary):
    count=0
    for i in range(len(nr_binary)):
        if nr_binary[i] == '1':
            count += 1
    return count

number = int(input("numar: "))
nr_binary = number_binary(number)
print(problem_7(nr_binary))

#--------------------------------------------

#EXERCIUTL 8
def problem_8(text):
    return len(text.split(' '))

text = input("text: ")
print(problem_8(text))