#from... import
#from total_sales import calculate_total_sale
#from total_sales import calculate_total_sales_day

#Variables
programStatus = True
sistemStatus = True
saleStatus = True
addProducts = True
newSales = True
sales=[]
salesDay=[]
totalSales=0
totalDay=0

print("--------------------------------")
print("Daily Sales Record")

while programStatus:    #Starting the program
    while sistemStatus:   #Starting the system
        while saleStatus:   #Starting the sale
            print("")
            name=input("Please, Enter the product name: ")  #Input for product name
            price=input("Please, Enter the product value: ") #Input for product value
            quantity=input("Please, Enter the quantity of the product: ") #Input for product quantity

            sale=[name, price, quantity]   #Creating a list with the product details (this part is not implemented yet, the sale list is not being used)
            sales.append(sale)    #Adding the sale to the sales list (this part is not implemented yet, the sales list is not being used)
            print("Product added successfully!")   #Print a message confirming that the product was added successfully

            print("--------------------------------")
            addProduct=input("Want add more product? (Yes) or (No): ").lower() #Input for adding more products

            if addProduct == "yes": #If the user wants to add more products, the saleStatus will be True and the program will ask for the product details again
                saleStatus=True

            elif addProduct == "no":    #If the user doesn't want to add more products, the saleStatus will be False and the program will ask if the user wants to register a new sale
                saleStatus=False
                salesDay=sales   #Create a list with the sales of the day (this part is not implemented yet, the sales list is not being used)
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
                        salesDay=sales   #Create a list with the sales of the day (this part is not implemented yet, the sales list is not being used)
                    else:
                        print("--------------------------------")
                        print("Invalid option, try again")

            addProducts=True

        print("--------------------------------")
        for sale in sales:  
            number = sales.index(sale) + 1   #Get the index of the sale in the sales list and add 1 to it (this part is not implemented yet, the sales list is not being used)  
            print(f"Product {number}: {sale[0]}, Value: {sale[1]}, Quantity: {sale[2]}, Total: {float(sale[1]) * int(sale[2])}")   #Print the product details (this part is not implemented yet, the sales list is not being used)
            subTotalSale=float(sale[1]) * int(sale[2])   #Calculate the total sale for each product (this part is not implemented yet, the sales list is not being used)
            totalSales= totalSales + subTotalSale   #Calculate the total sales for the day by adding the total sale for each product (this part is not implemented yet, the sales list is not being used)
            
        print(f"Total sale is: {totalSales}")   #Print the total sale for each product (this part is not implemented yet, the sales list is not being used)
    
        while newSales: 
            print("--------------------------------")
            newSale=input("Want to register a new sale? (Yes) or (No): ").lower()   #Ask if the user wants to register a new sale
            if newSale == "yes":    #If the user wants to register a new sale, the saleStatus will be True and the program will ask for the product details again
                saleStatus=True
                newSales=False
            elif newSale == "no":   #If the user doesn't want to register a new sale, the saleStatus will be False and the sistemStatus will be False, ending the program
                saleStatus=False
                sistemStatus=False
                newSales=False
                sales.clear()   #Clear the sales list for the next sale (this part is not implemented yet, the sales list is not being used)
            else:
                print("Invalid option, try again")  #If the user enters an invalid option, the program will print an error message and ask for the input again
                saleStatus=False

        newSales=True

    #menu
    print("--------------------------------")
    print("Daily Sales Record")
    print("1. Register a new sale")
    print("2. View sales records")
    print("3. Exit")

    option=input("Please, select an option: ")    #Input for menu option

    if option == "1":   #If the user selects option 1, the program will start the sale process again
        sistemStatus=True
        saleStatus=True
    elif option == "2": #If the user selects option 2, the program will print the sales records (this part is not implemented yet)
        print("--------------------------------")
        print("Sales records")
        number=len(salesDay)   
        print(f"holaaaaa {number}") 
        for sale in salesDay:  
            number = salesDay.index() + 1   #Get the index of the sale in the salesDay list and add 1 to it (this part is not implemented yet, the salesDay list is not being used)  
            print(f"Product {number}: {sale[0]}, Value: {sale[1]}, Quantity: {sale[2]}, Total: {float(sale[1]) * int(sale[2])}")   #Print the product details (this part is not implemented yet, the salesDay list is not being used)
            subTotalSalesDay= float(sale[1]) * int(sale[2])   #Calculate the total sale for each product (this part is not implemented yet, the salesDay list is not being used)
            totalDay= totalDay + subTotalSalesDay   #Calculate the total sales for the day by adding the total sale for each product (this part is not implemented yet, the salesDay list is not being used)
        print(f"Total sales for the day: {totalDay}")   #Print the total sales for the day (this part is not implemented yet, the totalDay variable is not being used)
    elif option == "3": #If the user selects option 3, the program will print a goodbye message and end the program
        print("--------------------------------")
        print("Thank you for using the Daily Sales Record program. Goodbye!")
        programStatus=False
    else:
        print("Invalid option, try again")  #If the user enters an invalid option, the program will print an error message and ask for the input again

"""Mira, ten en cuenta que cuando realizas un nueva compra, a persar de terminar la anterior, 
el programa no borra los datos de la compra anterior, por lo que al momento de registrar una nueva compra, 
el programa sigue sumando los datos de la compra anterior, por lo que el total de la nueva compra 
es el total de la compra anterior más el total de la nueva compra, lo mismo pasa con las ventas del día, 
por lo que al momento de registrar una nueva venta, el programa sigue sumando los datos de la venta anterior, 
por lo que el total de las ventas del día es el total de las ventas del día anterior más el total de las 
ventas del día actual. Para solucionar esto, puedes agregar una función para limpiar los datos de la compra anterior 
y las ventas del día anterior al momento de registrar una nueva compra o una nueva venta."""