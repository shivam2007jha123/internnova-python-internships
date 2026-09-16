# Input, Output & Type Casting (20 Marks)

# Create a program that:

# Takes user input (Name, Age, City).
# Converts Age into an integer using type casting.
# Displays a formatted introduction.

# Example Output:

# Hello! My name is Ram.
# I am 21 years old.
# I live in Mumbai.


name=input("enter your name:")
age=int(input("enter your age:"))  # int convert the string into integer
city=input("enter your city:")
print("Hello! My name is", name)
print("I am", age, "years old.")
print("I live in", city)    
