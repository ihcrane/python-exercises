#!/usr/bin/env python
# coding: utf-8

# In[1]:


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# In[2]:


#How many students are there?
print(len(students))


# In[11]:


#How many students prefer light coffee? For each type of coffee roast?
preference = [n['coffee_preference'] for n in students]
light_preference = preference.count('light')
medium_preference = preference.count('medium')
dark_preference = preference.count('dark')
print(light_preference)
print(medium_preference)
print(dark_preference)


# In[65]:


#How many types of each pet are there?
horse_count = 0
cat_count = 0
dog_count = 0
pets = list(n['pets'] for n in students)
for n in range(len(pets)):
    i = pets[n]
    for x in i:
        if x['species'] == 'horse':
            horse_count += 1
        elif x['species'] == 'cat':
            cat_count += 1
        else:
            dog_count += 1

print(horse_count, cat_count, dog_count)


# In[67]:


#How many grades does each student have? Do they all have the same number of grades?
grades = [len(n['grades']) for n in students]

print(grades)


# In[108]:


#What is each student's grade average?
avg_grade = [sum(n['grades'])/len(n['grades']) for n in students]

print(avg_grade)


# In[88]:


#How many pets does each student have?
num_pets = [len(n['pets']) for n in students]
print(num_pets)


# In[77]:


#How many students are in web development? data science?
num_web_dev = [n['course'].count('web development') for n in students]
num_web_dev = sum(num_web_dev)

num_data_science = [n['course'].count('data science') for n in students]
num_data_science = sum(num_data_science)
print(num_web_dev, num_data_science)


# In[85]:


#What is the average number of pets for students in web development?
num_pets_wd = [len(n['pets']) for n in students if n['course'] == 'web development']
num_pets_wd = sum(num_pets_wd)/num_web_dev
print(num_pets_wd)


# In[134]:


#What is the average pet age for students in data science?
pets = [n['pets'] for n in students if n['course'] == 'data science']
avg_age = 0
pet_count = 0
for n in range(len(pets)):
    i = pets[n]
    for x in i:
        avg_age += x['age']
        pet_count += 1
print(avg_age/pet_count)


# In[93]:


#What is most frequent coffee preference for data science students?
preference = [n['coffee_preference'] for n in students if n['course'] == 'data science']
dark = preference.count('dark')
medium = preference.count('medium')
light = preference.count('light')
print(preference, 'Dark: ', dark, 'Medium: ', medium, 'Light: ', light)


# In[94]:


#What is the least frequent coffee preference for web development students?
preference = [n['coffee_preference'] for n in students if n['course'] == 'data science']
dark = preference.count('dark')
medium = preference.count('medium')
light = preference.count('light')
print(preference, 'Dark: ', dark, 'Medium: ', medium, 'Light: ', light)


# In[106]:


#What is the average grade for students with at least 2 pets?
avg_grade = [sum(n['grades'])/len(n['grades']) for n in students if len(n['pets']) >= 2]
print(avg_grade)


# In[110]:


#How many students have 3 pets?
three_pets = [len(n['pets']) for n in students if len(n['pets']) >=3]
print(len(three_pets))


# In[111]:


#What is the average grade for students with 0 pets?
avg_grade_no_pets = [sum(n['grades'])/len(n['grades']) for n in students if len(n['pets']) == 0]
print(avg_grade)


# In[115]:


#What is the average grade for web development students? data science students?
avg_grade_wb = [sum(n['grades'])/len(n['grades']) for n in students if n['course'] == 'web development']
avg_grade_ds = [sum(n['grades'])/len(n['grades']) for n in students if n['course'] == 'data science']
print(avg_grade_wb, '\n', avg_grade_ds)


# In[133]:


#What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
dark_coffee_grades = [n['grades'] for n in students if n['coffee_preference'] == 'dark']
highest_grade = 0
lowest_grade = 100
for n in dark_coffee_grades:
    if max(n) > highest_grade:
        highest_grade = max(n)
    if min(n) < lowest_grade:
        lowest_grade = min(n)

print(highest_grade - lowest_grade)


# In[137]:


#What is the average number of pets for medium coffee drinkers?
num_pets_medium_pref = [len(n['pets']) for n in students if n['coffee_preference'] == 'medium']
num_pets_mp = sum(num_pets_medium_pref)/medium_preference

print(num_pets_mp)


# In[139]:


#What is the most common type of pet for web development students?
horse_count = 0
cat_count = 0
dog_count = 0
pets = [n['pets'] for n in students if n['course'] == 'web development']
for n in range(len(pets)):
    i = pets[n]
    for x in i:
        if x['species'] == 'horse':
            horse_count += 1
        elif x['species'] == 'cat':
            cat_count += 1
        else:
            dog_count += 1
print('Horses:', horse_count, 'Cats:', cat_count, 'Dogs:', dog_count)


# In[143]:


#What is the average name length?
names = [n['student'] for n in students]
num_names = len(names)
for n in names:
    name_len += len(n)

print(name_len/num_names)


# In[146]:


#What is the highest pet age for light coffee drinkers?
pets = [n['pets'] for n in students if n['coffee_preference'] == 'light']
highest_age = 0
for n in range(len(pets)):
    i = pets[n]
    for x in i:
        if x['age'] > highest_age:
            highest_age = x['age']
print(highest_age)


# In[ ]:




