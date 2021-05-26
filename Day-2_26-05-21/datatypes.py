age = 21 # int
cpi = 8.90 # float
name = "Harshil" # string
skills = ["Python", "Java", "Django"] # list-mutable
no = (5, 3, 2, 1, 4) # tuple-ordered and unmutable
st_data = {'first_name': 'Harshil',
           'last_name': 'Padhiyar'} # Dictionary

print(name, age, cpi)
print(type(st_data))
print(isinstance(skills, int)) # return false bcoz it is list
print("Hi,", st_data['first_name'], st_data['last_name'])


