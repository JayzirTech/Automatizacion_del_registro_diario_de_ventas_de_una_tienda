#from... import

#Variables
programStatus = True
sistemStatus = True
saleStatus = True
addProducts = True

print()
print("Daily Sales Record")

while programStatus:    #Starting the program
    while sistemStatus:   #Starting the system
        while saleStatus:   #Starting the sale
            print()
            name=input("Please, Enter the product name: ")  #Input for product name
            price=input("Please, Enter the product value: ") #Input for product value
            quantity=input("Please, Enter the quantity of the product: ") #Input for product quantity
            addProduct=input("Want add more product? (Yes) or (No): ").lower() #Input for adding more products

            if addProduct == "yes": #If the user wants to add more products, the saleStatus will be True and the program will ask for the product details again
                saleStatus=True

            elif addProduct == "no":    #If the user doesn't want to add more products, the saleStatus will be False and the program will ask if the user wants to register a new sale
                saleStatus=False
            else:
                print("Invalid option, try again")  #If the user enters an invalid option, the program will print an error message and ask for the input again

                while addProducts:  #If the user enters an invalid option, the program will enter this loop until the user enters a valid option
                    addProduct=input("Want add more product? (Yes) or (No): ").lower()
                    if addProduct == "yes":
                        saleStatus=True
                        addProducts=False
                    elif addProduct == "no":
                        saleStatus=False
                        addProducts=False
                    else:
                        print("")
                        print("Invalid option, try again")

            addProducts=True

        print("")
        newSale=input("Want to register a new sale? (Yes) or (No): ").lower()   #Ask if the user wants to register a new sale
        if newSale == "yes":    #If the user wants to register a new sale, the saleStatus will be True and the program will ask for the product details again
            saleStatus=True
        elif newSale == "no":   #If the user doesn't want to register a new sale, the saleStatus will be False and the sistemStatus will be False, ending the program
            saleStatus=False
            sistemStatus=False
        else:
            print("Invalid option, try again")  #If the user enters an invalid option, the program will print an error message and ask for the input again
            saleStatus=False

    #menu
    print("")
    print("Daily Sales Record")
    print("1. Register a new sale")
    print("2. View sales records")
    print("3. Exit")

    option=input("Please, select an option: ")    #Input for menu option

    if option == "1":   #If the user selects option 1, the program will start the sale process again
        sistemStatus=True
        saleStatus=True
    elif option == "2": #If the user selects option 2, the program will print the sales records (this part is not implemented yet)
        print("Sales records are not available yet.")
    elif option == "3": #If the user selects option 3, the program will print a goodbye message and end the program
        print("")
        print("Thank you for using the Daily Sales Record program. Goodbye!")
        programStatus=False
    else:
        print("Invalid option, try again")  #If the user enters an invalid option, the program will print an error message and ask for the input again