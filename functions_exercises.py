#!/usr/bin/env python
# coding: utf-8

# In[1]:


#defining function
def is_two(n):
    #determining if input is 2 of any kind
    if n == 2 or n == '2' or n == 'two':
        #returning True if 2
        return True
    #returning False otherwise
    else:
        return False
#testing function
print(is_two(5))
print(is_two(2))
print(is_two('two'))
print(is_two('hello'))


# In[3]:


#defining function
def is_vowel(n):
    #testing if input is a vowel and returning True if vowel
    if n in '[aieouAIEOU]':
        return True
    #returning False otherwise
    else:
        return False
#testing function  
print(is_vowel('j'))
print(is_vowel('i'))
print(is_vowel('e'))


# In[4]:


#defining function
def is_consonant(n):
    #testing if input is a vowel and returning False 
    if is_vowel(n):
        return False
    #returning True if not a vowel
    else:
        return True
#testing function  
print(is_consonant('j'))
print(is_consonant('h'))
print(is_consonant('i'))


# In[6]:


#defining function
def capitalize_consonant(n):
    #taking first letter of input and testing if consonant
    if is_consonant(n[0]):
        #capitalizing input and returning it
        return(n.capitalize())
    #otherwise return the word without capitalizing
    else:
        return(n)
#testing function    
print(capitalize_consonant('igloo'))
print(capitalize_consonant('house'))


# In[42]:


#defining function
def calculate_tip(tip_percentage, bill):
    #mulitplying bill by tip percentage
    amount = bill * tip_percentage
    #return tip amount rounded to second decimal place
    return round(amount, 2)

#testing function
print(calculate_tip(.18, 20))
print(calculate_tip(.25, 50))
print(calculate_tip(.25, 800))


# In[44]:


#defining function
def apply_discount(price, discount):
    #subtracting the product of price and discount from the price
    final_price = price - (price * discount)
    #return final price after calculation
    return final_price

#testing function
print(apply_discount(45, .20))
print(apply_discount(100, .17))


# In[18]:


#defining function
def handle_commas(n):
    #removing commas
    num = n.replace(',', '')
    #return string without commas
    return num
#testing functions
print(handle_commas('5,000'))
print(handle_commas('17,538'))


# In[22]:


#defining function
def get_letter_grade(n):
    #testing input through if statment for each grade starting at less than 60
    if n <= 60:
        return 'F'
    elif n <= 70:
        return 'D'
    elif n <= 80:
        return 'C'
    elif n <= 90:
        return 'B'
    elif n <= 100:    #ending with up to 100
        return 'A'

#testing function
print(get_letter_grade(97))
print(get_letter_grade(88))
print(get_letter_grade(43))


# In[24]:


#defining function
def remove_vowels(n):
    #testing each letter of the input word
    for i in n:
        #determining if letter is a vowel
        if is_vowel(i):
            #if letter is vowel remove and reassing variable
            n = n.replace(i, '')
    #return string with no vowels
    return n
#testing function
print(remove_vowels('pineapple'))
print(remove_vowels('guava'))


# In[34]:


#defining function
def normalize_name(n):
    #determing if any non alpha numeric characters
    for i in n:
        #then removing if applicable
        if i in '?!@$%><.,':
            n = n.replace(i, '')
    #making string lowercase
    n = n.lower()
    #removing any leading or trailing white space
    n = n.strip()
    #replacing spaces between words an underscore
    n = n.replace(' ', '_')
    #return final string
    return n
    
#testing function    
print(normalize_name('   % first name '))
print(normalize_name('codeup?'))
print(normalize_name('James Bond'))


# In[41]:


#defining function
def cumulative_sum(n):
    #declaring variables
    x = 0
    new_list = []
    #adding each number of list to each other one at a time
    for i in n:
        x += i
        #after adding each number to each other appending to a new list
        new_list.append(x)
    #return the new list
    return new_list
#testing function
print(cumulative_sum([1, 1, 1]))
print(cumulative_sum([2, 5, 7]))


# In[ ]:




