# EXERCITIUL 1
from typing import Counter

def problem1(n):
    fib_sir = []
    if n <= 0:
        return fib_sir
    a, b = 0, 1
    
    for i in range(n):
        fib_sir.append(a)
        a, b = b, a + b
    return fib_sir

n = int(input("n="))
print(problem1(n))

#-----------------------------------------------------

# EXERCITIUL 2
def nr_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range (3, n//2+1, 2):
        if n % i == 0:
            return False
    return True

def problem2(sir):
    sir_nr_prime = []
    for i in sir:
        if nr_prime(i):
            sir_nr_prime.append(i)
    return sir_nr_prime

sir = list(map(int, input("sir=").split()))
print(problem2(sir))

#-----------------------------------------------------

# EXERCITIUL 3
def problem3(a,b):
    # a intersected with b, a reunited with b, a - b, b - a
    a_inters_b = []
    a_reunit_b = []
    a_minus_b = []
    b_minus_a = []
    for i in a:
        if i in b:
            a_inters_b.append(i)
        a_reunit_b.append(i)
    for i in b:
        if i not in a:
            a_reunit_b.append(i)
            b_minus_a.append(i)
    for i in a:
        if i not in b:
            a_minus_b.append(i)
    return a_inters_b, a_reunit_b, a_minus_b, b_minus_a

a = list(map(int, input("a=").split()))
b = list(map(int, input("b=").split()))
print(problem3(a,b))

#-----------------------------------------------------

# EXERCITIUL 4
def problem4(musicalNotes,moves,start):
    song = []
    song.append(musicalNotes[start])
    for i in range(len(moves)):
        start = (start + moves[i]) % len(musicalNotes)
        song.append(musicalNotes[start])
    return song

musicalNotes = list(map(str, input("musicalNotes=").split())) 
moves = list(map(int, input("moves=").split()))
start = int(input("start="))
print(problem4(musicalNotes,moves,start))

#-----------------------------------------------------

# EXERCITIUL 5
def problem5(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i > j:
                a[i][j] = 0
    return a

a = [[1,2,3],[4,5,6],[7,8,9]]
print(problem5(a))

#-----------------------------------------------------

# EXERCITIUL 6
def problem6(x, liste):
    toate_elementele = []
    for lista in liste:
        toate_elementele.extend(lista)
    numaratori = Counter(toate_elementele)
    rezultat = []
    for element, numar in numaratori.items():
        if numar == x:
            rezultat.append(element)
    return rezultat

x = int(input("x="))
nr_liste = int(input("nr_liste="))
liste = []
for i in range(nr_liste):
    lista = list(map(str, input("lista=").split()))
    liste.append(lista)
print(problem6(x,liste))

#-----------------------------------------------------

# EXERCITIUL 7
def test_palindrom(n):
    invers = 0
    copie = n
    while copie > 0:
        invers = invers * 10 + copie % 10
        copie = copie // 10
    if invers == n:
        return True
    return False
def problem7(a):
    nr_palindrom = []
    rez=[]
    for i in a:
        if test_palindrom(i):
            nr_palindrom.append(i)
    rez.append(len(nr_palindrom))
    max=0
    for i in range(len(nr_palindrom)):
        if nr_palindrom[i]>max:
            max=nr_palindrom[i]
    rez.append(max)
    return rez

a=list(map(int, input("a=").split())) 
print(problem7(a))

#-----------------------------------------------------

# EXERCITIUL 8
def problem8(x=1, a=[], flag=True):
    rez = []
    for string in a:
        temp = []
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    temp.append(char)
            else:
                if ord(char) % x != 0:
                    temp.append(char)
        rez.append(temp)
    
    return rez

x = 2
a = ["test", "hello", "lab002"]
flag = False
print(problem8(x, a, flag))

#-----------------------------------------------------

# EXERCITIUL 9
def problem9(heights):
    blocked_seats = []
    for i in range(1, len(heights)):
        for j in range(len(heights[i])):
            for k in range(i):
                if heights[k][j] >= heights[i][j]:
                    blocked_seats.append((i, j))
                    break
    return blocked_seats

a=[[1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]] 
print(problem9(a))

#-----------------------------------------------------

# EXERCITIUL 10
def problem10(lists):
    max_len = max([len(lst) for lst in lists])
    result = []
    for i in range(max_len):
        temp_tuple = []
        for lst in lists:
            if i < len(lst):
                temp_tuple.append(lst[i])
            else:
                temp_tuple.append(None)
        result.append(tuple(temp_tuple))
    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
print(problem10([list1, list2, list3]))

#-----------------------------------------------------

# EXERCITIUL 11
def problem11(a):
    a.sort(key=lambda x: x[1][2])
    return a

a=[('abc', 'bcd'), ('abc', 'zza')]
print(problem11(a))

#-----------------------------------------------------

# EXERCITIUL 12
def problem12(words):
    result = []
    while words:
        word = words.pop(0)
        if len(word) < 2:
            continue
        rhyme = word[-2:]
        rhyme_group = [word]
        
        i = 0
        while i < len(words):
            if words[i][-2:] == rhyme:
                rhyme_group.append(words.pop(i)) 
            else:
                i += 1
        result.append(rhyme_group)
    return result

words = ['ana', 'banana', 'carte', 'arme', 'parte']
print(problem12(words))
