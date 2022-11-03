#!/usr/bin/env python
# coding: utf-8

# In[1]:


type(99.9)


# In[2]:


type('False')


# In[3]:


type(False)


# In[4]:


type('0')


# In[5]:


type(0)


# In[6]:


type(True)


# In[7]:


type('True')


# In[8]:


type([{}])


# In[9]:


type({'a': []})


# In[ ]:


#A term or phrase typed into a search box?: a string
#If a user is logged in?: a boolean
#A discount amount to apply to a user's shopping cart?: an integer
#Whether or not a coupon code is valid?: a boolean
#An email address typed into a registration form?: a string
#The price of a product?: a float
#A Matrix?: a list
#The email addresses collected from a registration form?: a string
#Information about applicants to Codeup's data science program?: a dictionary


# In[10]:


'1' + 2


# In[11]:


6 % 4


# In[12]:


type(6 % 4)


# In[13]:


type(type(6 % 4))


# In[15]:


'3 + 4 is ' + 3 + 4


# In[16]:


0 < 0


# In[17]:


'False' == False


# In[18]:


True == 'True'


# In[19]:


5 >= -5


# In[20]:


True or '42'


# In[21]:


6 % 5


# In[22]:


5 < 4 and 1 == 1


# In[23]:


'codeup' == 'codeup' and 'codeup' == 'Codeup'


# In[24]:


4 >= 0 and 1 != '1'


# In[25]:


6 % 3 == 0


# In[26]:


5 % 2 != 0


# In[27]:


[1] + 2


# In[28]:


[1] + [2]


# In[29]:


[1] * 2


# In[30]:


[1] * [2]


# In[32]:


[] + [] == []


# In[33]:


{} + {}


# In[ ]:


little_mermaid = 3
brother_bear = 5
hercules = 1
total_cost = (little_mermaid * 3) + (brother_bear * 3) + (hercules * 3)

print(total_cost)


# In[ ]:


google = 400
amazon = 380
facebook = 350
total_profit =(google * 6) + (amazon * 4) + (facebook * 10)

print(total_profit)


# In[34]:


class_is_full = True
schedule_is_full = False

can_enroll = schedule_is_full and not class_is_full

print(can_enroll)


# In[35]:


premium_member = True
discount_expired = False
num_items = 3

discount_applied = (premium_member or (num_items > 2)) and not discount_expired

print(discount_applied)


# In[53]:


username = 'codeup'
password = 'notastrongpassword'
username_white_space = (username[0] != ' ') and (username[-1] != ' ')
password_white_space = (password[0] != ' ') and (password[-1] != ' ')

password_len = 5 <= len(password) <= 20
not_same_as = username == password
print(password_len)
print(not_same_as)
print(username_white_space)
print(password_white_space)


# In[ ]:




