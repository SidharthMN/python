'''
print("Zero Division Error")

try:
    value_1 = 10
    value_2 = 0
    value_3 = value_1 / value_2
    print(value_3)
except ZeroDivisionError:
    print("Denominator cannot be zero")

print("\nType Error")

try:
    num1 = 15
    num2 = "25"
    add = num1 + num2
    print(add)
except TypeError:
    print("Unsupported operand type")

print("\nIndex Error")

appointment_id = [101, 102, 103, 104]

try:
    print(appointment_id[8])
except IndexError:
    print("Index out of range")

print("\nKey Error")

book_details = {
    "book_id": 21,
    "book_name": "Chronicles of Narnia",
    "book_author": "Joseph Claude"
}

try:
    print(book_details["ISBN No"])
except KeyError:
    print("Key not found")

print("\nFile Not Found Error")

try:
    with open("sample_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found in directory")

print("\nImport Error")

try:
    from math import squ
except ImportError as e:
    print(e)

print("\nValue Error")

try:
    greet = int("hello")
except ValueError:
    print("Invalid literal for int()")

print("\nAttribute Error")

user_value = "Welcome"

try:
    print(user_value.add())
except AttributeError as e:
    print(e)

print("\nName Error")

try:
    print(person)
except NameError as e:
    print(e)

print("\nMultiple Exception Handling")

try:
    greet = int("hello")
    from math import square
except (ValueError, ImportError) as e:
    print(e)

print("\nFinally Block Example")

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

try:
    quotient = numerator / denominator
    print("Quotient =", quotient)
except ZeroDivisionError as e:
    print(e)
finally:
    print("Executed normally")

print("\nLinear Search")

user_marks = list(map(int, input("Enter the elements: ").split()))
search_element = int(input("Enter the element to search: "))

for i in range(len(user_marks)):
    if user_marks[i] == search_element:
        print(f"Element found at position {i + 1}")
        break
else:
    print("Element not found")
'''

