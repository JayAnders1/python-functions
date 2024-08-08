
the_list = ['apple', 'banana', 'bread']

def shopping_list():
    
    while(True):

        print ("1. Add Item ")
        print ("2. Remove Item ")
        print ("3. View Shopping List")
        print ("4. Finish")

        choice = (input("Enter your choice (1/2/3/4): "))

        if choice == '1':
            add_item = input("What would you like to add to the shopping list?: ")
            the_list.append(add_item)
            print (f"{add_item} has been added to the shopping list! ")

        elif choice == '2':
            remove_item = input("What would you like to remove from the shopping list?: ")
            if remove_item in the_list:
                the_list.remove(remove_item)
            print (f"{remove_item} has been removed from the shopping list! ")

        elif choice == '3':
            print("Current shopping list: \n")
            for items in the_list:
                print (items)

        elif choice == '4':
            print ("Closing shopping list...")
            break

shopping_list()