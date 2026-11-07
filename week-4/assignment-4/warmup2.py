#subject contains a list inside the dictionary.
student = {
    "name": "Rebecca",
    "grade": 95,
    "subjects": ["Chemistry", "Mathematics", "Biology"]
}

for key, value in student.items():
    print(key, ":", value)
#False has no quotation marks since it is a Boolean value, not a string of text.
student["graduated"] = False

print(student)
