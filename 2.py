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
