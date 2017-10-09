list1 =[1,2,3]
list1[4] #Raises Index Error

dict1 = {1:'One',2:'Two'}
dict1[3] #Raises Key Error

print(marks) #Raises a Name Error

2 + "xyz" #Raises Type Error

int("a") #Raises Value Error

x = 10
x/0 #Raises ZeroDivisionError

for x [1,2,3]: #Raises SyntaxError

dir(__builtins__)

try:
    x = int(input("x: "))
    y = int(input("y: "))
    div = x/y
    print(div)
except ZeroDivisionError:
    print("Cannot Divide with Zero")
except ValueError:
    print("Only Integers allowed")
except:
    print("Unknown Error")
else:#executed only if there are no exceptions
    print("else block")
finally: #executed at the end by default
    print("Finally Block")


