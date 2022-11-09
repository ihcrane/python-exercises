#!/usr/bin/env python
# coding: utf-8

# In[11]:


import functions_exercises as fe

fe.is_vowel('a')


# In[13]:


from functions_exercises import calculate_tip

calculate_tip(.20, 120)


# In[16]:


from functions_exercises import get_letter_grade as lg

lg(97)


# In[5]:


from itertools import product

list(product('ABC', [1,2,3]))


# In[8]:


from itertools import combinations

list(combinations('abcd', 2))


# In[9]:


from itertools import permutations

list(permutations('abcd', 2))


# In[3]:


import json

dict_1 = json.load(open('profiles.json'))

print(len(dict_1))


# In[12]:


count = 0
for n in dict_1:
    if n['isActive']:
        count += 1
print(count)


# In[11]:


count = 0
for n in dict_1:
    if n['isActive'] == False:
        count += 1
print(count)


# In[10]:


total = 0
for n in dict_1:
    total += float(n['balance'].replace('$', '').replace(',', ''))
    
print(total)


# In[9]:


avg_bal = 0
for n in dict_1:
    avg_bal += float(n['balance'].replace('$', '').replace(',', ''))
    
print(round(avg_bal/len(dict_1), 2))


# In[13]:


lowest = 5000
lowest_name = ''

for n in dict_1:
    bal = float(n['balance'].replace('$', '').replace(',', ''))
    
    if bal < lowest:
        lowest_name = n['name']
        lowest = bal

print(lowest_name, lowest)


# In[14]:


highest = 1000
highest_name = ''

for n in dict_1:
    bal = float(n['balance'].replace('$', '').replace(',', ''))
    
    if bal > highest:
        highest_name = n['name']
        highest = bal

print(highest_name, highest)


# In[58]:


fruits = [n['favoriteFruit'] for n in dict_1]

sb_count = fruits.count('strawberry')
ap_count = fruits.count('apple')
ba_count = fruits.count('banana')


print('strawberry:', sb_count, 'apple:', ap_count, 'banana:', ba_count)


# In[15]:


greetings = [n['greeting'] for n in dict_1]
total = 0

for n in greetings:
    place = n.find('unread')
    total += int(n[place-3:place])

print(total)


# In[ ]:




