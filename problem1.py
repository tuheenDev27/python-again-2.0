'''
store data in a dictionary and check condition using if else statment

'''
data = {
    name: "tuhin",
    age: 22,
    status: "single",
    college: "Persidency college"
    school: "bathangachi high school"
}

if data["age"] > 22 and data["college"] == "Persidency college":
    print("you are eligible for this job")
else:
    print("you are not eligible for this job")