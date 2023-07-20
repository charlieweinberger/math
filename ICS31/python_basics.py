import random
from collections import namedtuple

def variablesAndArithmetic():

    print('')

    x = 5
    y = 4

    print(f"x = {x}")
    print(f"y = {y}")

    # Arithmetic (+ – * / % //)
    
    print(f"\nx + 5 = {x + 5}")
    print(f"x - 5 = {x - 5}")
    print(f"x * 5 = {x * 5}")
    print(f"x / 5 = {x / 5}") # returns a float
    print(f"x % 5 = {x % 5}") # mod
    print(f"x // 5 = {x // 5}") # returns an int

    # comparison (< <= == >= > !=)

    print(f"\nx < y: {x} < {y}: {x < y}")
    print(f"x <= y: {x} <= {y}: {x <= y}")
    print(f"x == y: {x} == {y}: {x == y}")
    print(f"x >= y: {x} >= {y}: {x >= y}")
    print(f"x > y: {x} > {y}: {x > y}")
    print(f"x != y: {x} != {y}: {x != y}")

    print('')

def strings():

    string = "Hello World!"
    
    # [start:stop:step]

    print(string[1:])
    print(string[:2])
    print(string[::2])
    print(string[::-1])

    # split() strip() upper() lower() replace()

    print(string.split(" "))
    print(string.strip()) # gets rid of spaces at the start & end of a string
    print(string.upper())
    print(string.lower())
    print(string.replace("o", "a"))

    # maketrans(), translate()

    string = "Hello Sam!"
    table = str.maketrans("S", "P")

    print(table)
    print(string.translate(table))

    # format()

    string1 = "My name is {fname}, I'm {age}".format(age = 36, fname = "John")
    string2 = "My name is {}, I'm {}".format("John", 36)

    print(string1)
    print(string2)

def ifElifElse():
    
    x = False
    y = False

    if x and y:
        print("x and y")
    elif x or y:
        print("x or y")
    else:
        print("neither x nor y")

def listsAndLoops():

    a = [1, 2, 3, 5, 71]

    for elem in a:
        print(elem)

    b = [0, 5, 1, 65]
    i = 0

    while i < len(b):
        print(b[i])
        i += 1

    # list() append() extend() sort() sorted() count()

    fruits = list(('apple', 'banana', 'cherry'))
    print(fruits)

    fruits.append("orange")
    print(fruits)

    cars = ['Ford', 'BMW', 'Volvo']
    fruits.extend(cars) # the cars go AFTER the fruits
    print(fruits)

    fruits.sort()
    print(fruits)

    new_cars = sorted(cars)
    print(f"{cars}")
    print(f"{new_cars}")

    x = fruits.count("cherry")
    print(x)

def dictionaries():
    
    dictionary = {"hello": "goodbye", "one": "two", "taco": "bell"}

    print(dictionary)
    print(dictionary["hello"])
    print(dictionary.items())
    print(dictionary.keys())
    print(dictionary.values())

    dictionary["fruit"] = "apple"

    print(dictionary)

def sets():
    
    set1 = {"apple", "banana", "cherry"}
    set2 = set((1, 2, 3, 3))

    print(set1)
    print(set2)

    set3 = {3, 2, 1}

    print(set3)
    print(set2 == set3)

def pythonMethods():
    
    # len() input() print() range() int() float() str() set() randrange()
    
    x = [1, 2, 3]
    print(len(x))

    # x = input("What is your name? ")
    print(x)

    r = list(range(0, 20, 2))
    print(r)

    r = random.randrange(3, 7) # random INTEGER between 3 and 6
    print(r)

def files():
    
    # "r" - Read   - Opens a file for reading, error if the file does not exist (default)
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write  - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists
    # "t" - Text   - Text mode (default)
    # "b" - Binary - Binary mode (e.g. images)

    # write

    g = open("./ICS31/demo.txt", "w")
    g.write("I added this line!")
    g.close()

    # read

    f = open("./ICS31/demo.txt", "r")

    print(f.read())
    # print(f.readline())
    # print(f.readlines())

    f.close()

def namedtuples():
    
    Student = namedtuple("Student", "name ID GPA year")

    s1 = Student("Smith, Paula", 11112222, 3.95, 1997)
    s2 = Student("Johnson, Calvin", 22223333, 3.22, 1996)

    print(s1)
    print(s2)

    # for student in [s1, s2]:
    #     print(f"The student {student.name} has ID {student.ID}, GPA {student.GPA}, and was born in {student.year}.")
    
    s2 = s2._replace(GPA = 4.0)
    
    print(s2)

def assertStatement():
    
    x = 5

    assert True
    assert x < 10

    assert x > 10

# variablesAndArithmetic()
# strings()
# ifElifElse()
# listsAndLoops()
# dictionaries()
# sets()
# pythonMethods()
# files()
# namedtuples()
# assertStatement()