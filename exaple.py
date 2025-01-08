# 1. Variables and Type Casting

integer_var = 5
float_var = 10.5
string_var = "20"
print(f"Type of integer_var: {type(integer_var)}")
print(f"Type of float_var: {type(float_var)}")
print(f"Type of string_var: {type(string_var)}")
converted_int = int(string_var)
print(f"Converted string to integer: {converted_int}")
converted_float_to_int = int(float_var)
print(f"Converted float to integer: {converted_float_to_int}")

# 2. Conditionals and Loops

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
even_sum = 0
for i in range(2, number + 1, 2):  
    even_sum += i

print(f"The sum of all even numbers from 1 to {number} is: {even_sum}")

# 3. Function
def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum
numbers_list = [1, 2, 3, 4, 5, 6]
even_sum, odd_sum = sum_even_odd(numbers_list)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

# 4. File Handling
with open("sample.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")
with open("sample.txt", "r") as file:
    content = file.read()
    print("Contents of sample.txt:")
    print(content)

# 5. Object-Oriented Programming (OOP)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
rect = Rectangle(5, 10)
print(f"The area of the rectangle is: {rect.calculate_area()}")

# 6. Error Handling
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of division is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
