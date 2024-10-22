def problem1(a,b):
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

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(problem1(a,b))

def problem2(a):
    d = {}
    for char in a:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d
print(problem2("Ana are mere"))

def problem3(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    if dict1.keys() != dict2.keys():
        return False

    for key in dict1:
        val1, val2 = dict1[key], dict2[key]

        if isinstance(val1, dict) and isinstance(val2, dict):
            if not problem3(val1, val2):
                return False

        elif isinstance(val1, list) and isinstance(val2, list):
            if val1 != val2:
                return False

        elif isinstance(val1, set) and isinstance(val2, set):
            if val1 != val2:
                return False

        elif val1 != val2:
            return False

    return True

d_1 = {'a': {'b': 0}, 's': 4, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
d_2 = {'a': {'a': 3}, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
print(problem3(d_1, d_2))

def problem4(tag, content, **dict):
    xml = '<' + tag
    for (key, val) in dict.items():
        xml += ' ' + key + '="'+val + '"'
    xml += "> " + content + " </" + tag + ">"
    return xml

print(problem4("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

def problem5(rules, dict):
    for tup in rules:
        if tup[0] not in dict.values():
            return False
        content = dict[tup[0]]
        if not content.startswith(tup[1]):
            return False
        if not content.endwith(tup[3]):
            return False
        if content.startswith(tup[2]) or content.endswith(tup[2]):
            return False
        if content.find(tup[2]) < 1:
            return False
    return True

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(problem5(s, d))

def problem6(a):
    unique_elements = set()
    duplicate_elements = set()

    for item in a:
        if item in unique_elements:
            duplicate_elements.add(item)
        else:
            unique_elements.add(item)

    a = len(unique_elements) - len(duplicate_elements)
    b = len(duplicate_elements)
    
    return a, b

print(problem6([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]))

def problem7(*sets):
    result = dict()
    list_of_sets = list()
    for singular_set in sets:
        list_of_sets.append(singular_set)
    for i in range(len(list_of_sets)):
        for j in range(i + 1, len(list_of_sets)):
            if list_of_sets[i] != list_of_sets[j]:
                result[str(list_of_sets[i]) + ' | ' + str(list_of_sets[j])] = \
                    list_of_sets[i].union(list_of_sets[j])
                result[str(list_of_sets[i]) + ' & ' + str(list_of_sets[j])] = \
                    list_of_sets[i].intersection(list_of_sets[j])
                result[str(list_of_sets[i]) + ' - ' + str(list_of_sets[j])] = list_of_sets[i] - list_of_sets[j]
                result[str(list_of_sets[j]) + ' - ' + str(list_of_sets[i])] = list_of_sets[j] - list_of_sets[i]
    return result

print(problem7({1,2,3}, {3,4,5}))

def problem8(mapping):
    current = 'start'
    visited = [current]
    values = list()
    while True:
        current = mapping[current]
        if current in visited:
            return values
        visited.append(current)
        values.append(current)

print(problem8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

def problem9(*positions, **arguments):
    count = 0
    for p in positions:
        if p in arguments.values():
            count += 1
    return count

print(problem9(1, 2, 3, 4, x=1, y=2, z=3, w=5))