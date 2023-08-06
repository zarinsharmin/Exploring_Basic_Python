#Task-1. variable manipulation

def task1():
    name = 'Zarin'
    age = 23

    print ("My name is " + name + " and I am " +str(age)+ " years old ")
    

#Task-2: Data type and Data Types and Type Conversion
def task2():
    num1 = 10
    num2 = 10.5
    num1_float = float(num1)
    num2_int = int(num2)
    print("num1 :", num1)
    print("num1_float :", num1_float)
    print("num2 :", num2)
    print("num2_int :", num2_int)

     

#Task-3:
def task3_string_manipulation():

    sentence = "\"Python programming is fun!\""
    print("Length of" +sentence+ "is:" +str(len(sentence)))

    print("8th charecter of " +sentence+ "is :" +str(sentence[8]))

    substring = sentence[1:7]

    print(" I enjoy it!" +substring)

#Task 4: Lists and List Manipulation
def task4_Lists_and_List_Manipulation():
    fruits = [ "apple", "banana", "cherry", "date"]
    fruits.append("grape")
    fruits.remove("banana")
    print(len(fruits))
    sliced_fruits = fruits[2:4]
    # slice_fruits = fruits[2,3]

    extra_fruits = ["kiwi","lemon"]
    combined_fruits = sliced_fruits + extra_fruits
    print (sliced_fruits)
    print (combined_fruits)

#Task 5: Conditional Statements

def task5_Conditional_Statements():
    num = 5
    mod = num % 2
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")

#Task 6: Loops
def task6_Loops():
    for num in range (1,11):
        print(num)   

    i = 0
    sum = 0
    while (i <= 100) :
        sum = sum + i
        i = i + 1
    print("sum is " , sum)

    
#Task 7:
def task7_calculate_square(num):
    num = int(num)
    print("Square is " , (num*num) )

def is_prime (num):
    num = int(num)
    i = 2
    t = 0
    while (i <= (num/2)) :
        if (num % i == 0) :
            t = 1
        i = i + 1

    if (t == 1) :
        print("This number is not prime")
    else :
        print("This number is prime")


#Task 8 :Dictionary 

def task8():
    student = {
        "name" : "Sharmin" ,
        "age" : 24 ,
        "grade" : "1st Class"
    }
    student["course"] = "DDMS"
    print(student)
    print("All key-value pairs: ")
    for i,j in student.items():
        print(i,j)


task1()
task2()
task3_string_manipulation()
task4_Lists_and_List_Manipulation()
task5_Conditional_Statements()
task6_Loops()
task7_calculate_square(7)
is_prime(29)
task8()
    

