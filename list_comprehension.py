#!/usr/bin/env python
# coding: utf-8

# In[59]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# In[60]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. 
#Make a variable named uppercased_fruits to hold the output of the list comprehension. 
#Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [n.upper() for n in fruits]
print(uppercased_fruits)


# In[61]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to 
#produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [n.capitalize() for n in fruits]
print(capitalized_fruits)


# In[80]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
#Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels = [n for n in fruits if (n.count('a') + n.count('e') + 
                                                          n.count('i') + n.count('o') + n.count('u')) > 2]
print(fruits_with_more_than_two_vowels)


# In[81]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [n for n in fruits if (n.count('a') + n.count('e') + 
                                                          n.count('i') + n.count('o') + n.count('u')) == 2]
print(fruits_with_only_two_vowels)


# In[83]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_len_more_than_5 = [n for n in fruits if len(n) > 5]
print(fruits_len_more_than_5)


# In[84]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_len_5 = [n for n in fruits if len(n) == 5]
print(fruits_len_5)


# In[85]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_len_less_than_5 = [n for n in fruits if len(n) < 5]
print(fruits_len_less_than_5)


# In[86]:


# Exercise 8 - Make a list containing the number of characters in each fruit. 
#Output would be [5, 4, 10, etc... ]
fruits_len = [len(n) for n in fruits]
print(fruits_len)


# In[87]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [n for n in fruits if n.count('a') >= 1]
print(fruits_with_letter_a)


# In[89]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)


# In[90]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [n for n in numbers if n % 2 == 1]
print(odd_numbers)


# In[91]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)


# In[92]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [n for n in numbers if n < 0]
print(negative_numbers)


# In[93]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
num_len = [n for n in numbers if len(str(n)) > 1]
print(num_len)


# In[95]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [n ** 2 for n in numbers]
print(numbers_squared)


# In[97]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n > 0 and n % 2 == 1]
print(odd_negative_numbers)


# In[98]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [n + 5 for n in numbers]
print(numbers_plus_5)


# In[113]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
primes = [n for n in numbers if n > 1 and all(n % x != 0 for x in range(2, n))]
print(primes)

