#expense tracker
import numpy as np
expensetrack=[]
while True:
    print("item purchased/ money spend on which:")
    print('price of the iten or how much money spended:')
    print('end')
    number=input('enter no.')
    if number=='1':
            itembought  =input('enter money spend on which item/ price as well:')
            expensetrack.append(itembought)
            print('add all')
    elif number=='2':
        print('your expense tracker with price 1:')
        for allitem in expensetrack:
            print('-',allitem)
    elif number=='3':
        break
    else:
        print("not available number")
            
    
            