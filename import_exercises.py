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


# In[6]:


from itertools import product

list(product('ABCD', '123'))


# In[8]:


from itertools import combinations

list(combinations('abcd', 2))


# In[9]:


from itertools import permutations

list(permutations('abcd', 2))


# In[2]:


import json

dict_1 = json.load(open('profiles.json'))

print(len(dict_1))


# In[24]:


num = 0
for n in dict_1:
    if n['isActive']:
        num += 1
print(num)


# In[71]:


num = 0
for n in dict_1:
    if n['isActive'] == False:
        num += 1
print(num)


# In[10]:


total = 0
for n in dict_1:
    total += float(n['balance'].replace('$', '').replace(',', ''))
    
print(total)


# In[9]:


total = 0
for n in dict_1:
    total += float(n['balance'].replace('$', '').replace(',', ''))
    
print(round(total/len(dict_1), 2))


# In[11]:


lowest = 10000
lowest_name = ''

for n in dict_1:
    num = float(n['balance'].replace('$', '').replace(',', ''))
    
    if num < lowest:
        lowest_name = n['name']
        lowest = num

print(lowest_name, lowest)


# In[12]:


highest = 1000
highest_name = ''

for n in dict_1:
    num = float(n['balance'].replace('$', '').replace(',', ''))
    
    if num > highest:
        highest_name = n['name']
        highest = num

print(highest_name, highest)


# In[58]:


fruits = [n['favoriteFruit'] for n in dict_1]

sb_count = fruits.count('strawberry')
ap_count = fruits.count('apple')
ba_count = fruits.count('banana')


print('strawberry:', sb_count, 'apple:', ap_count, 'banana:', ba_count)


# In[13]:


greetings = [n['greeting'] for n in dict_1]
total = 0

for n in greetings:
    spot = n.find('unread')
    total += int(n[spot-3:spot])

print(total)


# In[ ]:




