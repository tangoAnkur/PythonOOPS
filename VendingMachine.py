class VendingMachine(object):

    totalRevenue = 0 # Total revenue of all vending machines in the system

    snackPrices = {"candy": 2.00, "soda": 1.50, "chips": 3.00, "cookies": 3.50}

    # Instance attributes
    def __init__(self, inventory, serial, daysUntilMaintenance):
        self.inventory = inventory # dictionary with {<snack>: <amount>} as key-value pairs. Possible snacks: candy, soda, chips, cookies. Keys written in lowercase.
        self.revenue = 0           # Initially, when an instance of the vending machine is created, the revenue is 0 and it's updated with each sale.
        self.serial = serial
        self.daysUntilMaintenance = daysUntilMaintenance

    # Method that displays an interactive menu to process a sale.
    # Displays the options, gets user input to select the snack, and calls
    # another method to process the sale.
    def salesMenu(self):

        # The user has the option to buy several types of snacks
        # so the program is repeated if the user indicates that he/she
        # would like to buy another snack
        while True:

            greetings = "\nWelcome! I have:\n"
            request = "\nPlease enter the number of the item: "

            # Print a welcome message with the snacks available
            print(greetings)

            i = 1
            for snack in self.inventory:
                print("(" + str(i) + ") " + snack.capitalize())
                i += 1

            # Get the user input (option selected)
            custInput = int(input(request))

            # Repeat if the input doesn't meet the requirements
            while custInput <= 0 or custInput > len(self.inventory):
                print("Please enter a number from 1 to", len(self.inventory))
                # Get the user input (option selected)
                custInput = int(input(request))
        
            # Display appropriate message
            self.processSale(list(self.inventory.keys())[custInput - 1].lower())
            answer = int(input("\nWould you like to buy another snack?\nEnter 1 for YES and 0 for NO: "))

            # If the customer does not wish to buy another snack
            if not answer:
                break


    # Method that processes the sale by asking the user how many snacks of that type
    # he/she would like to buy and calls another method to opdate the inventory
    def processSale(self, option): # option must be in lowercase
        
        print("\nYou selected: %s" % option.capitalize())
        
        if self.inventory[option] > 0:
            
            # Display current snack inventory and product
            print("Great! I currently have %d %s in my inventory\n" % (self.inventory[option], option))
            
            # Ask for the number of snacks
            numItems = int(input("How many %s would you like to buy?\n" % option))

            # Handle cases where user might enter a negative number or zero
            while numItems <= 0:
                print("Please enter a positive integer")
                numItems = int(input("\nHow many %s would you like to buy?\n" % option))

            # Update inventory if there are enough snacks available
            if numItems <= self.inventory[option]:
                self.removeFromInventory(option, numItems)
                
                # Update the machine's revenue
                total = self.updateRevenue(option, numItems)

                print("That would be: $ " + str(total))

                # Display a message confirming the purchase and current inventory
                print("\nThank you for your purchase!")
                print("Now I have %d %s and my revenue is $%d" % (self.inventory[option], option, self.revenue))
                
            else:
                print("I don't have so many %s. Sorry! :(" % option)
                
        else:
            print("I don't have any more %s. Sorry! :(" % option)


    # Method that updates the vending machine's (instance) inventory by
    # decrementing the availability of the snack chosen.
    def removeFromInventory(self, option, numItems):
        self.inventory[option] -= numItems

    # Update the revenue of the instance of VendingMachine
    # and update the class attribute total revenue.
    def updateRevenue(self, option, numItems):
        # Find price of the snack
        price = self.findSnackPrice(option)

        # Update Instance and class
        self.revenue += numItems * price
        VendingMachine.totalRevenue += numItems * price

        return numItems * price

    # Find the price of the snack selected in the class attribute
    # and return it
    def findSnackPrice(self, snack):
        return VendingMachine.snackPrices[snack]        
        
    # Method that prints a message with the total revenue of the instance of VendingMachine
    def displayRevenue(self):
        print("The total revenue of this vending machine is:", self.revenue)
                      

# Subclasses =============================================================================================
            

class HospitalVendingMachine(VendingMachine):

    # Complete the class

        

class SchoolVendingMachine(VendingMachine):

    # Complete the class


# Instances =============================================================================================

floor1Machine = VendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "011423424", 24)
##floor1Machine.initialMenu()

hospital1Machine = HospitalVendingMachine({"candy": 32, "soda": 50, "chips": 45, "cookies": 80}, "03223424", 15)
##hospital1Machine.initialMenu()

school1Machine = SchoolVendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "0534424", 2)
school1Machine.initialMenu()



