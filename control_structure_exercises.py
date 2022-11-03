#!/usr/bin/env python
# coding: utf-8

# In[45]:


day_of_the_week = str(input())
if day_of_the_week == 'Monday':
    print(f'Today is {day_of_the_week}.')
else:
    print('Today is not Monday!')


# In[43]:


if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    print('It is the weekend.')
else:
    print('Today is a weekday.')


# In[15]:


hours_worked = 45
hourly_rate = 30
paycheck = 0
overtime = 0
if hours_worked > 40:
    overtime = hours_worked - 40
    hours_worked -= overtime

paycheck = (hours_worked * hourly_rate) + (overtime * (hourly_rate * 1.5))
print(paycheck)


# In[18]:


i = 5
while i <= 15:
    print(i)
    i += 1


# In[19]:


i = 0
while i <= 100:
    print(i)
    i += 2


# In[20]:


i = 100
while i >= -10:
    print(i)
    i -= 5


# In[21]:


i = 2
while i <= 1000000:
    print(i)
    i **= 2


# In[23]:


i = 100
while i > 0:
    print(i)
    i -= 5


# In[40]:


i = int(input())
for n in range(1, 11):
    
    print(i, 'x ', f'{n} =', i * n)


# In[39]:


for n in range(1, 10):
    print(n*f'{n}')


# In[46]:


print('Input a positive integer:')
i = int(input())
while i >= 1:
    print(i)
    i -= 1


# In[49]:


print('Input a positive integer:')
i = int(input())
n = 0
while n <= i:
    print(n)
    n += 1


# In[60]:


print('Input an odd number between 1 and 50')
i = input()
if i.isdigit() != True:
    print('Make sure you entered a valid input!:')
    i = int(input())
else:
    i = int(i)
for n in range (1, 50):
    if n % 2 == 1:
        if n == i:
            print('Yikes! Skipping number:', i)
        else: 
            print('Heres an odd number:', n)


# In[2]:


i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    i += 1


# In[37]:


while True:
    i = int(input('What number would you like to go up to? '))
    print('Here is your table!')
    print('number | squared| cubed')
    print('------ | -------| ------')
    n = 1
    while n <= i:
        print(f'{n}\t|{n**2}\t|{n**3}')
        n += 1
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break


# In[34]:


while True:
    print('Enter a numerical grade:')
    i = int(input())
    if 100 >= i >= 88:
        print('A')
    elif 87 >= i >= 80:
        print('B')
    elif 79 >= i >= 67:
        print('C')
    elif 66 >= i >= 60:
        print('D')
    elif i <= 59:
        print('F')
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break


# In[46]:


books = [{
        'title': 'Harry Potter',
        'author': 'J.K. Rowling',
        'genre': 'fantasy',
    },
    {
        'title': 'Percy Jackson',
        'author': 'Rick Riordan',
        'genre': 'greek mythology',
    },
    {
        'title': 'Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'genre': 'fantasy'
    },
    {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'genre': 'fiction'
    }]

requested_genre = input('What genre are you interested in? ')
requested_books = [n['title'] for n in books if n['genre'] == requested_genre]

print(requested_books)


# In[ ]:




