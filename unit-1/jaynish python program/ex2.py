# Program to demonstrate different data types and type casting

# Different data types
integer_value = 10
float_value = 10.5
string_value = "Python"
boolean_value = True
complex_value = 3 + 2j

print("Integer:", integer_value)
print("Float:", float_value)
print("String:", string_value)
print("Boolean:", boolean_value)
print("Complex:", complex_value)

# Type casting
num1 = "100"
num2 = "25.5"

integer_num = int(num1)
float_num = float(num2)
string_num = str(integer_value)

print("\n--- Type Casting ---")
print("String to Integer:", integer_num)
print("String to Float:", float_num)
print("Integer to String:", string_num)

# Checking data types
print("\n--- Data Types ---")
print(type(integer_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))
print(type(complex_value))