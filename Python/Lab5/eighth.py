person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# I. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"Middle skill: {skills[middle_index]}")
# II. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python skill exists')
    else:
        print('Python skill does not exist')
# III. Determine the title based on the skills
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('Unknown title')
# IV. If the person is married and lives in Finland, print the information in the specified format
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
