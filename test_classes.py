from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

ar10 = Arithmetic(5,10)
print(ar10.add())
print(ar10.subtract())
print(ar10.multiply())
print(ar10.divide())
print(ar10.remainder())
ar10.print_self()

ar3 = Arithmetic(3,6)
print(ar3.add())
print(ar3.subtract())
print(ar3.multiply())
print(ar3.divide())
print(ar3.remainder())
ar3.print_self()

ar50 = Arithmetic(50,255)
print(ar50.add())
print(ar50.subtract())
print(ar50.multiply())
print(ar50.divide())
print(ar50.remainder())
ar50.print_self()