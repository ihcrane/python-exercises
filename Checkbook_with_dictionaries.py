#!/usr/bin/env python
# coding: utf-8

# In[19]:


from datetime import datetime

checking_account = 100.00                  #declaring variables
debit = 0
credit = 0
transactions = []
num_deposits = 0
num_withdrawls = 0
desc = ''
while True:                                                #while loop to keep program going until user exits
    print('What would you like to do\n\n'                  #getting the input from user of first choice
          '1) view current balance\n'
            '2) record a debit (withdrawl)\n'
            '3) record a credit (deposit)\n'
            '4) view transaction history\n'
            '5) modify transaction\n'
            '6) exit\nYour choice?')
    choice = input()
    if choice == '1' or choice in 'view current balance':                 #first choice of checking account balance
        print(f'Your current balance is ${checking_account:.2f}')
    elif choice == '2' or choice in 'record a debt (withdrawl)':
        debit = input('How much is the debit? ')                  #second choice of making a withdrawl
        if debit.isdigit() != True:
            debit = float(input('Please only enter a number.'))
        checking_account -= float(debit)
        desc_choice = input('Would you like to add a description?(y/n) ')    #asking user if they would like to
        if desc_choice == 'y' or desc_choice == 'yes':                                               #add a description
            desc = input('Please input description:')
        transactions.append({'transaction_type':'withdrawl',
                             'amount':f'${debit}',
                             'timestamp':str(datetime.today())[:19],
                             'description':desc})                  #inputing description
    elif choice == '3' or choice in 'record a credit (deposit)':                                         #third choice of making a deposit
        credit = input('How much is the credit? ')  
        if credit.isdigit() != True:
            credit = float(input('Please only enter a number.'))
        checking_account += float(credit)
        desc_choice = input('Would you like to add a description?(y/n) ')    #asking user if they would like to
        if desc_choice == 'y' or desc_choice == 'yes':                                               #add a description
            desc = input('Please input description:')
        transactions.append({'transaction_type':'deposit',
                             'amount':f'${credit}',
                             'timestamp':str(datetime.today())[:19],
                             'description':desc}) 
    elif choice == '4' or choice in 'view transaction history':                  #fourth choice of viewing past transactions
        category = input('Which category?:\n'
                        '1) Deposits\n'               #selecting which category to view
                        '2) Withdrawls\n'
                        '3) Per day\n'
                        '4) Keyword\n'
                        '5) All\n')
        if category == '1' or category in 'deposits':
            print('Your deposit history:')           #first category is deposit history
            for n in transactions:
                if n['transaction_type'] == 'deposit':
                    print(n['amount'] + ' ' + n['timestamp'] + ' ' + n['description'])
                    num_deposits += 1
            deposit_stats = (num_deposits/(len(transactions))) * 100     #stats of number of deposits
            print(f'{deposit_stats}% of your transactions are deposits.')
        elif category == '2' or category in 'withdrawls':
            print('Your withdrawl history:')          #second category is withdrawl history
            for n in transactions:
                if n['transaction_type'] == 'withdrawl':
                    print(n['amount'] + ' ' + n['timestamp'] + ' ' + n['description'])
                    num_withdrawls += 1
            withdrawl_stats = (num_withdrawls/(len(transactions))) * 100      #stats of number of withdrawls
            print(f'{withdrawl_stats}% of your transactions are withdrawls.')
        elif category == '3' or category in 'per day':
            day = input('Please input the date you wish to view (YYYY-MM-DD):\n')
            print(f'Your transaction history for {day}')                    #third category is viewing transactions
            for n in transactions:                                         #by date
                if day in n['timestamp']:
                    print(n['amount'] + ' ' + n['timestamp'] + ' ' + n['description'])
        elif category == '4' or category in 'keyword':
            keyword = input('Please enter keyword:')            #fourth category is viewing transaction by keyword
            for n in transactions:
                if keyword in n['description']:
                    print(n['amount'] + ' ' + n['timestamp'] + ' ' + n['description'])
        elif category == '5' or category in 'all':                               #fifth category is viewing all transactions
            print('Your entire transaction history:')
            for n in transactions:
                print(n['amount'] + ' ' + n['timestamp'] + ' ' + n['description'])
    elif choice == '5' or choice in 'modify transactions':
        print('Your transaction history:')                  #fifth chioce is modifying transactions
        i = 1
        for n in transactions:
            print(i, ' ', n['amount'], ' ', n['timestamp'], ' ', n['description'])                               #listing and numbering all transactions 
            i += 1
        t_num = int(input('Please select which transaction number you wish to modify:\n'))
        ta = transactions[t_num-1]                                    #selecting which transaction to modify
        new_desc = input('Please enter the new description:\n')       #inputing new description from user
        transactions[t_num-1]['description'] = new_desc               #replacing all transaction with new
        for n in transactions:                                        #print new transaction history
            print(i, ' ', n['amount'], ' ', n['timestamp'], ' ', n['description'])
    elif choice == '6' or choice in 'exit':
        print('Thank you! Have a nice day.')                      #exiting program
        break
    else:
        print('Invalid input.\nTry again.')                   #else for invalid input of choice
        continue

        


# In[ ]:




