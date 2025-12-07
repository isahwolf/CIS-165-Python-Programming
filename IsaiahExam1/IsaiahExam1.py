#Isaiah Wolf 2/25/24
#IsaiahExam1.py

choice = 0
pounds = 0.0
price = 0.0
subtotal = 0.0
tax = 0.0
total = 0.0
TAX_RATE = 0.0925

def main():
    global choice, pounds, price, subtotal, tax, total
    display_menu() #calls method for menu
    choice = int(input('Please enter your choice.'))
    
    while choice !=6:
        if choice > 0 and choice < 6:
            pounds = float(input('Enter the pounds purchased :'))
            if pounds <= 0:
                print("Invalid input. Quantity must be greater than zero.")
                
            if choice == 1:   #apples
                price = 5.99
            elif choice == 2: #oranges
                price = 15.49
            elif choice == 3: #celery
                price = 14.99
            elif choice ==4:  #potatoes
                price = 1.99
            elif choice == 5: #mushrooms
                price = 3.89
                
            subtotal += price * pounds
        else:
                print('Incorrect entry.\nTry again.')
                
        display_menu()  #calls method for menu
        choice = int(input('Please enter your choice.'))

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print ('Subtotal:      $', format(subtotal, ',.2f'))
    print ('Tax:           $', format(tax, ',.2f'))
    print ('Total Sale:    $', format(total, ',.2f'))

def display_menu(): #method for menu
    print('Enter 1 for Apples')
    print('Enter 2 for Oranges')
    print('Enter 3 for Celery')
    print('Enter 4 for Potatoes')
    print('Enter 5 for Mushrooms')
    print('Enter 6 for Exit')
main()
