def format_my_test():
    print(
    '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
    '''
)
format_my_test()

def menu():
    
    
    appetizersList = {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0}
    entreesList = {'Salmon': 0, 'Steak': 0,'Meat Tornado': 0, 'A Literal Garden': 0}
    dessertsList = {'Ice Cream': 0, 'Cake': 0, 'Pie': 0}
    drinksList = {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
    categoryMenu = [appetizersList, entreesList, dessertsList, drinksList]

    loops = 20
    inputs = []
    quantity=0

    for x in range(loops):
        order = str(input("> "))
        if(order =='quit' or order =='q'):
            quit()
        inputs.append(order)
       
        if(order in inputs[x]):
            quantity+=1
        elif(not order in inputs[x]):
            quantity=0
        print(f"** {quantity} order of {inputs[x]} have been added to your meal **")
        
menu()