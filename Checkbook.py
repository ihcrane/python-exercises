#!/usr/bin/env python
# coding: utf-8

# In[38]:


from datetime import datetime

checking_account = 100.00                  #declaring variables
debit = 0
credit = 0
transactions = []
transactions.append(f'${checking_account}')
num_deposits = 0
num_withdrawl = 0
while True:                                                #while loop to keep program going until user exits
    print('What would you like to do\n\n'                  #getting the input from user of first choice
          '1) view current balance\n'
            '2) record a debit (withdrawl)\n'
            '3) record a credit (deposit)\n'
            '4) view transaction history\n'
            '5) modify transaction\n'
            '6) exit\nYour choice?')
    choice = input()
    if choice == '1':                                             #first choice of checking account balance
        print(f'Your current balance is ${checking_account:.2f}')
    elif choice == '2':
        debit = float(input('How much is the debit? '))                  #second choice of making a withdrawl
        checking_account -= debit
        withdrawl = '-$' + str(debit) + ' ' + str(datetime.today())[:19]
        desc_choice = input('Would you like to add a description?(y/n) ')    #asking user if they would like to
        if desc_choice == 'y':                                               #add a description
            desc = input('Please input description:')
            withdrawl = withdrawl + ' Description: ' + desc                  #inputing description
        transactions.append(withdrawl)
    elif choice == '3':                                         #third choice of making a deposit
        credit = float(input('How much is the credit? '))  
        checking_account += credit
        deposit = '+$' + str(credit) + ' ' + str(datetime.today())[:19]
        desc_choice = input('Would you like to add a description?(y/n) ')    #asking user if they would like to
        if desc_choice == 'y':                                               #add a description
            desc = input('Please input description:')
            deposit = deposit + ' Description: ' + desc                      #inputing description
        transactions.append(deposit)
    elif choice == '4':                                #fourth choice of viewing past transactions
        category = input('Which category?:\n'
                        '1) Deposits\n'               #selecting which category to view
                        '2) Withdrawls\n'
                        '3) Per day\n'
                        '4) Keyword\n'
                        '5) All\n')
        if category == '1':
            print('Your deposit history:')           #first category is deposit history
            for n in transactions:
                if n[0] == '+':
                    print(n)
                    num_deposits += 1
            deposit_stats = (num_deposits/(len(transactions)-1)) * 100     #stats of number of deposits
            print(f'{deposit_stats}% of your transcations are deposits.')
        elif category == '2':
            print('Your withdrawl history:')          #second category is withdrawl history
            for n in transactions:
                if n[0] == '-':
                    print(n)
                    num_withdrawls += 1
            deposit_stats = (num_withdrawls/(len(transactions)-1)) * 100      #stats of number of withdrawls
            print(f'{deposit_stats}% of your transcations are withdrawls.')
        elif category == '3':
            day = input('Please input the date you wish to view (YYYY-MM-DD):\n')
            print(f'Your transaction history for {day}')                    #third category is viewing transactions
            for n in transactions:                                         #by date
                if n[-19:-9] == day:
                    print(n)
        elif category == '4':
            keyword = input('Please enter keyword:')            #fourth category is viewing transaction by keyword
            for n in transactions:
                if keyword in n:
                    print(n)
        elif category == '5':                               #fifth category is viewing all transactions
            print('Your entire transaction history:')
            for n in transactions:
                print(n)
    elif choice == '5':
        print('Your transaction history:')                  #fifth chioce is modifying transactions
        i = 1
        for n in transactions:
            print(i, ' ', n)                               #listing and numbering all transactions 
            i += 1
        t_num = int(input('Please select which transaction number you wish to modify:\n'))
        ta = transactions[t_num-1]                                    #selecting which transaction to modify
        print(ta)
        new_desc = input('Please enter the new description:\n')       #inputing new description from user
        t_index = ta.find('Description:')                             #finding index of current description
        new_t = ta[:t_index+13] + new_desc                            #replacing old description with new
        transactions[t_num-1] = new_t                                 #replacing all transaction with new
        for n in transactions:                                        #print new transaction history
            print(n)
    elif choice == '6':
        print('Thank you! Have a nice day.')                      #exiting program
        break
    else:
        print('Invalid input.\nTry again.')                   #else for invalid input of choice
        continue

        


# 

# In[ ]:




