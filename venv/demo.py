from math import *

print("Hello there world")
#declare a variable
name = "John"
Age = "35"
print("There was a man called," + name )
print("He was " + Age + " years old")

#you can change a variable
name = "Howdy"
print("He really liked the name " + name)
print("But didnt like being " + Age)

phrase = "I am Isabel"
#changes a variable to an upper case and confirms true or false
print(phrase.upper().isupper())

#checks the length of a character
print(len(phrase))

#a string gets indexed starting with zero so it will check the index of a character
print(phrase [2])

#index function-: tell us where the specific character or string is located inside our strings
print(phrase.index("I")) #passing a parameter

#replace will replace a character/string
print(phrase.replace("Isabel", "Ann"))

#basics of using numbers
print(3*5)
print(3.234567766)
print(3 + 7)
print(5/3)
print(3 * 4 + 5)
print(3 * (2 + 4))
print(10 % 3) #modulus

#numbers can be storred inside variables
my_num = 3
print(my_num)

#convert the number into a string
print(str(my_num) + " is my favourite number") #anytime you convert a number into a string, you must use str

#common functions in python related to numbers
#abs (absolute value)

my_num = -6
print(abs(my_num))
#pow, (power function)allow you to give a number 2 pieces of information,  or to the power of;
print(pow(3, 2)) # same sa 3^2(raised to)

#max function returns the larger number
print(max(10, 5))
print(min(6, 3)) # prints minimum number
print(round(3.78965)) #rounds it off

my_num= 5
print(floor(3.7)) #grabs the lowest number
print(ceil(3.4)) #Rounds the number off to the next number
print(sqrt(36)) #returns the square root

print(fabs(9))

name = input("Enter your name : ")
print("Hello " + name )
