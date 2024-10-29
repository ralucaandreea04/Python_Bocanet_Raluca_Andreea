#Exercitiul 1
def problem1():
    class Stack:
        def __init__(self):
            self.stack = []
        def push(self, data):
            self.stack.append(data)
        def pop(self):
            if len(self.stack) == 0:
                return None
            return self.stack.pop()
        def peek(self):
            if len(self.stack) == 0:
                return None
            return self.stack[-1]
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.peek())
print("Stack:")
problem1()

#Exercitiul 2
def problem2():
    class Queue:
        def __init__(self):
            self.queue = []
        def push(self, data):
            self.queue.append(data)
        def pop(self):
            if len(self.queue) == 0:
                return None
            return self.queue.pop(0)
        def peek(self):
            if len(self.queue) == 0:
                return None
            return self.queue[0]
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.peek())
print("Queue:")
problem2()

#Exercitiul 3
def problem3():
    class Matrice:
        def __init__(self, n, m):
            self.n=n
            self.m=m
            self.matrice = [[0 for j in range(m)] for i in range(n)]
        def get(self, i, j):
            return self.matrice[i][j]
        def set(self, i, j, value):
            self.matrice[i][j] = value
        def transpose(self):
            transposed = Matrice(self.m, self.n)
            for i in range(self.n):
                for j in range(self.m):
                    transposed.set(j, i, self.get(i, j))
            return transposed
        def multiply(self, other):
            if self.m != other.n or self.n != other.m:
                return None
            result = Matrice(self.n, other.m)
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        result.matrice[i][j] += self.matrice[i][k] * other.matrice[k][j]
            return result
        def function(self, f):
            for i in range(self.n):
                for j in range(self.m):
                    self.matrice[i][j] = f(self.matrice[i][j])
    m = Matrice(2, 2)
    m.set(0, 0, 1)
    m.set(0, 1, 2)
    m.set(1, 0, 3)
    m.set(1, 1, 4)
    print(m.get(0, 0))
    print(m.get(0, 1))
    print(m.get(1, 0))
    print(m.get(1, 1))
    print(m.transpose().matrice)
    print(m.multiply(m).matrice)
    m.function(lambda x: x * 2)
    print(m.matrice)
print("Matrix:")
problem3()