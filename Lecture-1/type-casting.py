"""
Type casting / conversion: 
- it is the process of converting data from one data type to the other data type 
note: the data should be convertable to the target form 
ex: "hello" -> int ? no 
   "1.5" -> float ? yes 
   "1.5" -> int ? no 

int(data) -> any data into integer 
ex: int("1") -> 1 
float(data) -> any data into float 
str(data) -> any data into string 
bool(data) -> any data into bool 
"""
name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter Height (in feet): "))
gender = input("Enter Gender (male/female): ")

print(type(name)) # str 
print(type(age)) # int 
print(type(height)) # float 
print(type(gender)) # str 