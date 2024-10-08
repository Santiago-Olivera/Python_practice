'''
1. Variables
a. Multiple Choice:
Which of the following is a valid variable name in Python?

A) 2nd_place
B) first-place
C) _secondPlace
D) third Place

ANSWER: C

2. Loops
a. Short Answer:
Explain the difference between a for loop and a while loop in Python.

For loop repeats a specific number of times , while loop iterates until a condition is met. 

3. Conditionals
a. Coding Exercise:
Write a Python function named check_number that takes an integer as input and prints:

"Positive" if the number is greater than zero,
"Negative" if the number is less than zero,
"Zero" if the number is exactly zero.
'''

def check_number(n:int):
    if(n>0):
        print("Positive")
    elif(n<0):
        print("Negative")
    else: 
        print("Zero")

check_number(0)

'''
4. Functions
a. Multiple Choice:
What will be the output of the following code?
def add(a, b=5):
    return a + b

result = add(10)
print(result)
A) 10
B) 15
C) Error
D) 5

ANSWER : B) 15

5. File I/O
a. Short Answer:
Describe the purpose of the with statement when working with files in Python.

I think is to define an alias, like ''with [file name] as'' , but I'm not sure

6. Coding Exercise: Comprehensive
Write a Python program that:

Prompts the user to enter their name.
Saves the name to a file called names.txt.
Reads all names from names.txt and prints them, each on a new line.
'''

username = input("Enter your name: ")
with open("names.txt", "a") as file:
    file.write(username + "\n")

with open("names.txt", "r") as file:
    names = file.readlines()

for name in names:
    print(name.strip())

'''
7. Bonus Question: Variables and Loops
a. Coding Exercise:
Create a Python script that initializes a variable count to 0. Use a for loop 
to iterate over the numbers from 1 to 10. For each number, add it to count. 
After the loop finishes, print the final value of count.
count = 0 
for i in range(1,11):
    count += i
print(count)


8 .  The benefit of using functions with conditional statements, lies in the posibility 
combine the reusability of code that is provided by functions , and the flow control of the
code execution with the conditional statements . 

9. File I/O Error Handling
a. Coding Exercise:
Modify the following code to include error handling using try-except blocks to handle
 the case where the file data.txt does not exist.

'''
try:
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("file does not exist")

'''
10. Advanced Loop Usage
a. Multiple Choice:
Which keyword can be used to skip the current iteration and continue with the next one in a loop?

A) pass
B) break
C) continue
D) exit

Answer : C) continue
'''


