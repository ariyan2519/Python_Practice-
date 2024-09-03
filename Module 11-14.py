#Module_11
#What are strings
#Triple Single Quote

name = input("What is your name? ")
print("Hello,", name,name,'is from "Bangladesh"' )
print('''Hi .this is ariyan.
I am from Bangladesh.
My home town is B-Baria'''
)

#Module_12
#For loop
#Strings

Country = "Bangladesh"
Hometown = "B-Baria"
Age = "18"
Description = '''Hi this is ariyan. I am from Bangladseh. I am going to B-baria for travel'''
print(Country[0])
print(Country[1])
print(Country[2])

for character in Age:
    print(character)


#Module_13
#Sting Slicing Methods
name  = input("What is your name? ")
print(len(name))
print(name[0:-2])
print(name[-4:-2])

#Module_14
#String Methods
Country = "bangladesh is a beautiful country"
print(Country.capitalize())
print(Country.upper())
print(Country.lower())
print(Country.title())
print(Country.split())

#Using f function in python
x = "Hello world"
y = x.casefold()
print(f"so the result is : {y}")
#Using Count Method
friend = "Emon and ariyan are are friends!"
result_friend = friend.count("are")
print(f"Now the final result is : " ,{result_friend})

#Using "endswoth" method

z = "Hello World"
if z.endswith("World"):
    print("True")
else:
    print("False")

#Using "join" method 
my_list = ["ariyan","emon"]
my_list_1 = "--".join(my_list)
print(my_list_1)


#Module_14
#If-Else Statement
number = int(input("Please input your age: "))

if number <= 57:
    print("You can drive a car!")
else:
    print("You can't drive a car!")



