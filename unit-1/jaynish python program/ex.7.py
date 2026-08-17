# 7.Write a program to create a dictionary and  demonstrate dictionary methods and iteration.
student = {
    "name": "jaynish",
    "age": 20,
    "course": "Python"
}

print("Dictionary =", student)

print("Name =", student["name"])

student["age"] = 21
student["city"] = "Rajkot"

print("After update =", student)

print("Keys =", student.keys())
print("Values =", student.values())
print("Items =", student.items())

print("Iteration:")

for key, value in student.items():
    print(key, "=", value)