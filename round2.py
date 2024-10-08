'''
Question 1: Data Structures
What are Python dictionaries, and how do they differ from lists? 
Can you provide an example of a scenario where you'd prefer to use a dictionary 
over a list?

Python dictionarios a datatype that consist of key,value pairs, basically allows you
to map values with keys, allowing easy retrieval of information. 
Well lists are associate with specific index, so in a list the 'key' to access the store
value would be the index so to speak . while in dictionaries the key might be anything you
want to define . 

An example could be :
mapping names and phone numbers or id values. like : 
contacts = {
    "santiago": 123456,
    "Juan" : 324252, 
    "German" : 2209919
}
while you could achieve a similar behavior, its more optimal to use dictionaries. 

'''

'''
Question 2: Coding Challenge

Write a Python function that takes a string and returns
 a new string where every character is repeated twice.
'''

def repeat(x):
    '''
    x --> string input
    output --> string where each character of x is repeated twice
    '''
    result = ""
    for i in x:
        result+=i*2
    return result


'''
Question 3: Object-Oriented Programming (OOP)

What is the purpose of classes and objects in Python? Can you 
write a small Python class called Car that has attributes make,
model, and year, and includes a method display_info() to print out the car's information?

the purpose of classes and objects, is to be able to use the adventages of OOP. 
wich emulates real life behaviour, like in the challenge car, where we're defining 
attributes that cars has in general . Then we could create an instance of the specific car
for example toyota, and all cars would have this same blueprint, but might have different 
values in its attributes. 
'''
class Car:
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(self.make)
        print(self.model)
        print(self.year)

#creating an instance of the class
toyota = Car("Toyota", "Corolla", 2020)
toyota.display_info()

