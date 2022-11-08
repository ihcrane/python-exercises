
#!/usr/bin/env python
# coding: utf-8

# In[29]:


money_dict = [{'name': 'twenty', 'plural': 'twenties', 'value': 0},       #dictionary to set singular and plural
              {'name': 'ten', 'plural': 'tens', 'value': 0},             #names for money types as well as amounts
              {'name': 'five', 'plural': 'fives', 'value': 0},
              {'name': 'one', 'plural': 'ones', 'value': 0},
              {'name': 'quarter', 'plural': 'quarters', 'value': 0},
              {'name': 'dime', 'plural': 'dimes', 'value': 0},
              {'name': 'nickel', 'plural': 'nickels', 'value': 0},
              {'name': 'penny', 'plural': 'pennies', 'value': 0}]


def dollar_calc(dollars):        #function for dollar calculation
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    n = 0
    dollars = int(dollars)
    while dollars > 0:                #while loop to check number of bills total
        if dollars >= 20:           #first if statement to check number of twenties 
            dollars -= 20 
            twenties += 1
        elif dollars >= 10:        #second if statement to check number of tens
            dollars -= 10
            tens += 1
        elif dollars >= 5:        #third if statement to check number of fives
            dollars -= 5
            fives += 1
        elif dollars >= 1:         #fourth if statement to check number of ones
            dollars -= 1
            ones += 1
    dollar_list = [twenties, tens, fives, ones]       
    for bills in money_dict:                    #for loop to reassign bills values inside the dictionary
        if n <= 3:
            bills['value'] = dollar_list[n]
        n += 1

def coin_calc(coins):          #function for coin calculation
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    n = 0
    coins = int(coins)
    while coins > 0:         #while loop to determine number of each coin
        if coins >= 25:      #if statement to determine number of quarters
            coins -= 25
            quarters += 1
        elif coins >= 10:       #if statement to determine number of dimes
            coins -= 10
            dimes += 1
        elif coins >= 5:     #if statement to determine number of nickels
            coins -= 5
            nickels += 1
        elif coins >= 1:      #if statement to determine number of pennies
            coins -= 1
            pennies += 1
    coin_list = [quarters, dimes, nickels, pennies]      
    for coins in money_dict:                      #for loop to reassign coin values inside dictionary
        if n > 3:
            coins['value'] = coin_list[n-4]
        n += 1


total_price = float(input('Please input the total price: $'))         #taking input from user for total price
cash_given = float(input('Please input the total cash paid: $'))      #taking input from user for cash paid

def change_calc(price, cash):
    total_change = str(format((cash - price), '.2f'))              #determining total change
    split_list = total_change.split('.')
    dollars = split_list[0]                #setting dollars to equal only the whole numbers of the change
    coins = split_list[-1]                 #setting coins to equal the decimal numbers of the change
    
    dollar_calc(dollars)               #running total change through above functions
    coin_calc(coins)
    
    print(f'Your total change is $', total_change)           #print total change
            
    for money in money_dict:                         #for loop to determine if value is greater than 1
        if money['value'] > 1:
            print(money['value'], ' ', money['plural'])         #only prints from this line if it needs to be plural     
        
        elif money['value'] == 1:
            print(money['value'], ' ', money['name'])          #only prints from this line if not plural

        else:
            continue                                #doesn't print if value is equal to 0
    
    

change_calc(total_price, cash_given)


# In[ ]:





# In[ ]:




