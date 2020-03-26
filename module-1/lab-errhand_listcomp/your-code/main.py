#Example: 
"""
eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
"""
import os
import random
import sys
"""
#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [ (e+1)**2 for e in range(20)] # square from 1 to 20 
print("1. Square of 20 first numbers -> ")
print(square)

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two = [ 2**(e+1) for e in range(50) ]
print("2. First 50 power -> ") 
print(power_of_two)


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt = [(e+1)**0.5 for e in range(100) ]
print("3. Square root of first 100 -> " )
print(sqrt)

#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list=[ e for e in range(-10,1)]
print(" 4. Create a list")
print(my_list)


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results


odds = [ e for e in range(1,101) if e%2==1]
print(" 5. Find the odd numbers")
print(odds)



#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven=[ e for e in range(1,1001) if e%7==0]
print(" 6. Find divisibles by 7 ->")
print(divisible_by_seven)


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'

non_vowels=[ x for x in teststring if not x in set(["a","e","i","o","u"])]  
print("7. Remove all vowels -> ")
print(non_vowels)



#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

test_sentence="The Quick Brown Fox Jumped Over The Lazy Dog"

capital_letters=[ x for x in test_sentence if x.isupper()]
print("8. Find capital letters")
print(capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

test_sentence="The Quick Brown Fox Jumped Over The Lazy Dog"
consonants=[ x for x in test_sentence if not x in set(["a","e","i","o","u"," "])]

print(" 9. Find consonants: -> ")
print(consonants)


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.


arr1= [x for x in os.listdir("../") if os.path.isdir("../" + x) ]
arr2= [x for x in os.listdir("../../") if os.path.isdir("../../" + x) ]
arr3= [x for x in os.listdir("../../..") if os.path.isdir("../../../" + x) ]
arr=arr1+arr2+arr3
print(arr)


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_list = [ [ random.randrange(0,100) for x in range(10)]  for e in range(4) ]
print(random_list)



#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [x for e in list_of_lists for x in e]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [ float(x) for e in list_of_lists for x in e]
print(floats)



#14. Handle the exception thrown by the code below by using try and except blocks. 

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("one of the elements in the list has a type not supported")



#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Your are trying a division by zero")
    pass

print("All done")



#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    abc=[10,20,20]
    print(abc[3])
except IndexError:
    print("You want to print out of the range in the list")




#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

while True:
    try:
        number1=float(input("Give me the numerator number: "))
        number2=float(input("Give me the denominator number: "))
        respuesta=number1/number2
        print(f"The division of {number1} between {number2} is: {respuesta}")
        break
    except ValueError:
        print ("Please insert just numbers (if it's a float use '.' as a quote)")
    except ZeroDivisionError:
        print ("Please the second number must be different of zero")



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("The file doesn't exist!!")




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
    line = fp.readline()
    i = int(line.strip())
except FileNotFoundError:
    print("the file 'myfile.txt' is not here") 
except ValueError:
    print("the file doesn't have an int value")



#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('darwin' in sys.platform), "Function can only run on apple systems.... the dream of Jobs :)"
    print('Doing something.')

try:
    linux_interaction()
except AssertionError:
    print("Function can only run on apple systems.... the dream of Jobs") 




# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.


while True:
    try:
        number=float(input("Give me the number (must be integer): "))
        if number%1==0:
            respuesta=number**2
            print(f"The square of number is: {respuesta}")
            break
        else:
            print("The number must be an integer!")

    except ValueError:
        print ("Please insert just numbers (it should be integer)")


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

def div_exac(x):
    if [e for e in range(2,10) if x%e==0] == []:
        return False
    else:
        return True


results = [ x for x in range(1001) if div_exac(x)]
print(results)

"""
# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

while True:
    try:
        Total_Marks = int(input("Enter Total Marks Scored: ")) 
        Num_of_Sections = int(input("Enter Num of Sections: "))

        if Num_of_Sections<2:
            print("Please the num of sections must be greater than 1 ")
        elif Total_Marks<0:
            print("The Marks Scored must be positive")
        else:
            break
    
    except ValueError:
        print ("Please insert just numbers (it should be integer)")
