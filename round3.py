'''
Question 1: Functions and Scope

What is the difference between local and global variables in Python? 
Can you provide an example where a local and a global variable might conflict?

The difference is that a local variable , can only be accessed within the block scoped
in which its defined. On the other hand, a global can be access in all parts
for example : 
'''
'''globalVariable = "global!"
aux = False
if(aux):
    localVariable = "local!"
print(globalVariable)
print(localVariable) #When aux= False , localVariable is not created.
'''

'''
Question 2: Coding Challenge

Write a Python function that checks if a given number is a palindrome. 
A palindrome is a number that reads the same backward as forward.

'''
def check_palindrome(x):
    '''
    x --> integer number
    output --> boolean True if x is palindrome , otherwise false.
    '''
    print(str(x) == str(x)[::-1])
    return str(x) == str(x)[::-1]


'''
Question 3: File Handling

How do you read from and write to a file in Python? Can you write a simple 
program that reads from a file named input.txt, capitalizes each line, and 
writes the result to a new file called output.txt?

I don't remember the syntax , but I know that is something like : 
my_read = read(input.txt)
my_read.upper()
write(output.txt,my_read)
'''