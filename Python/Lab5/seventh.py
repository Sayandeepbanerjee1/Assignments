# Create a student dictionary and add keys with default values
student = {
    'first_name': '',
    'last_name': '',
    'gender': '',
    'age': 0,
    'marital_status': '',
    'skills': [],  # Skills should be a list
    'country': '',
    'city': '',
    'address': ''
}

# I. Get the length of the student dictionary
length_of_dict = len(student)
print(f"Length of student dictionary: {length_of_dict}")

# II. Get the value of skills and check the data type
skills_value = student['skills']
print(f"Value of 'skills': {skills_value}")
print(f"Data type of 'skills': {type(skills_value)}")

# III. Modify the skills values by adding one or two skills
student['skills'].extend(['Python', 'Data Analysis'])
print(f"Updated 'skills': {student['skills']}")

# IV. Get the dictionary keys as a list
keys_list = list(student.keys())
print(f"Dictionary keys: {keys_list}")

# V. Get the dictionary values as a list
values_list = list(student.values())
print(f"Dictionary values: {values_list}")

# VI. Change the dictionary to a list of tuples using _items()_ method
items_list = list(student.items())
print(f"Dictionary items as list of tuples: {items_list}")

# VII. Delete one of the items in the dictionary
# For example, delete 'age'
del student['age']
print(f"Dictionary after deleting 'age': {student}")

# VIII. Delete the student dictionary
del student
print("Student dictionary has been deleted.")
