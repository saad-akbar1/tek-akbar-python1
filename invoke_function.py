import importlib

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print("Invoking function with a mix of default arguments")
introduction_with_mix_of_default_args("John","Doe")
introduction_with_mix_of_default_args(first_name = "John")
introduction_with_mix_of_default_args("John",last_name = "Doe")

print("Invoking function for a product of two numbers")
print(product_of_two_num(5,6))

print("Invoking function for adding all numbers")
print(add_all_nums(1,2,3,4))

print("Invoking function for doubles")
print(double(6))

print("Invoking function for fibonacci function")
print(fib(3))

print("Invoking function for subtraction")
print(subtract(10,7))

print("Invoking function for testing palindrome")
print(pal("test"))
print(pal("racecar"))