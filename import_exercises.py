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

profiles = json.load(open('profiles.json'))

print(len(profiles))


# In[5]:


active = [n for n in profiles if n['isActive']]
len(active)


# In[7]:


not_active = [n for n in profiles if not n['isActive']]
len(not_active)


# In[8]:


total = 0
for n in profiles:
    total += float(n['balance'].replace('$', '').replace(',', ''))
    
print(total)


# In[11]:


avg_bal = 0
for n in profiles:
    avg_bal += float(n['balance'].replace('$', '').replace(',', ''))
    
print(round(avg_bal/len(profiles), 2))


# In[12]:


lowest = 5000
lowest_name = ''

for n in profiles:
    bal = float(n['balance'].replace('$', '').replace(',', ''))
    
    if bal < lowest:
        lowest_name = n['name']
        lowest = bal

print(lowest_name, lowest)


# In[13]:


highest = 1000
highest_name = ''

for n in profiles:
    bal = float(n['balance'].replace('$', '').replace(',', ''))
    
    if bal > highest:
        highest_name = n['name']
        highest = bal

print(highest_name, highest)


# In[14]:


fruits = [n['favoriteFruit'] for n in profiles]

sb_count = fruits.count('strawberry')
ap_count = fruits.count('apple')
ba_count = fruits.count('banana')


print('strawberry:', sb_count, 'apple:', ap_count, 'banana:', ba_count)


# In[15]:


greetings = [n['greeting'] for n in profiles]
total = 0

for n in greetings:
    place = n.find('unread')
    total += int(n[place-3:place])

print(total)


# In[ ]:




