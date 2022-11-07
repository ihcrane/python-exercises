#!/usr/bin/env python
# coding: utf-8

# In[72]:


def dollar_calc(dollars):        #function for dollar calculation
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
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
    return[twenties, tens, fives, ones]      #return number of each bill in a list

def coin_calc(coins):          #function for coin calculation
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
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
    return [quarters, dimes, nickels, pennies]      #return list of each number of coins


total_price = float(input('Please input the total price: $'))         #taking input from user for total price
cash_given = float(input('Please input the total cash paid: $'))      #taking input from user for cash paid

def change_calc(price, cash):
    total_change = str(round((cash - price), 2))    #determining total change
    split_list = total_change.split('.')
    dollars = split_list[0]                #setting dollars to equal only the whole numbers of the change
    coins = split_list[-1]                 #setting coins to equal the decimal numbers of the change

    
    dollar_list = dollar_calc(dollars)    #calling the dollar_calc function
    coin_list = coin_calc(coins)          #calling coin_calc function
    
    print(f'Your total change is ${total_change}')           #print total change
    
    if dollar_list[0] > 1:                           #if statement to determine if more then one of each bill
        print(dollar_list[0], "twenty dollar bills" )   #for printing line with or without plurals
    elif dollar_list[0] == 1:
        print(dollar_list[0], "twenty dollar bill")
    if dollar_list[1] > 1:
        print(dollar_list[1], "ten dollar bills" )     #for 10 dollar bills
    elif dollar_list[1] == 1:
        print(dollar_list[1], "ten dollar bill")
    if dollar_list[2] > 1:
        print(dollar_list[2], "five dollar bills" )    #for 5 dollar bills
    elif dollar_list[2] == 1:
        print(dollar_list[2], "five dollar bill")
    if dollar_list[3] > 1:
        print(dollar_list[3], "one dollar bills" )     #for 1 dollar bills
    elif dollar_list[3] == 1:
        print(dollar_list[3], "one dollar bill")
    
     
    if coin_list[0] > 1:                   #if statement to determine if more then one of each coin
        print(coin_list[0], "quarters" )     #for printing line with or without plurals
    elif coin_list[0] == 1:
        print(coin_list[0], "quarter")
    if coin_list[1] > 1:
        print(coin_list[1], "dimes" )        #for dimes
    elif coin_list[1] == 1:
        print(coin_list[1], "dime")
    if coin_list[2] > 1:
        print(coin_list[2], "nickels" )     #for nickels
    elif coin_list[2] == 1:
        print(coin_list[2], "nickel")
    if coin_list[3] > 1:
        print('and', coin_list[3], "pennies!" )   #for pennies!
    elif coin_list[3] == 1:
        print('and 1 penny!')

    
    

change_calc(total_price, cash_given)


# In[ ]:




