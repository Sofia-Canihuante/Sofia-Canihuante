# File: Project3.py
# Student: Sofia Canihuante
# UT EID: smc5865
# Course Name: CS303E
# 
# Date Created: November 30, 2024
# Description of Program: This porgram uses various classes with methods inside of it and functions using files that creates and then goes through a file and generates items from it to play market game. First 
# it generates a file filed with events which are interger datatypes and uses them to generate a list of these intergers based on the principle true or false of add customer. The classes
# then generate a populated list from the list of events with methods for said events to play the game and a customer class to insert customers with methods to play the game. The game is then played
# down below which uses various boolean, if statements, and loops to play the game based on the number of events. 


################################################################################
#                                                                              #
#                       Simulation of a Simple Market                          #
#                                                                              #
################################################################################

import random
import os.path

# The following function is useful and can be used as is;  there is no 
# reason to change it. 

def addCustomer( percent ):
    """This function returns True with a certain probability.  For
      example, if percent is 35, then this returns True 35% of the 
      times you call it and returns False 65% of the time. This is 
      a useful trick in a simulation. """
    return random.randint(0, 99) < percent

def generateEventsFile( N, perc, maxItems, fileName ):
    """Create a file of N lines to drive the simulation.  Each line in the
      file contains a single non-negative integer in range
      [0...maxItems].  Lines are non-zero perc percentage of the time.
      Use the function addCustomer( percent) to decide whether the
      item should be zero or a random integer between 1 and maxItems,
      inclusive.  The idea is that if a line is zero, no new customer
      has arrived during that clock tick.  Otherwise, a new customer
      has arrived at the cashier line with that many items in their
      basket.  Remember to close the file."""
    infile = open(fileName, "w") 
    for i in range(N):
        if addCustomer( perc ) == True:
          infile.write(str(random.randint(1, maxItems)))
          infile.write("\n")
        else:
          infile.write(str(0))
          infile.write("\n")
    infile.close()


def generateEventListFromFile( filename ):
    """Given a filename containing events, generate a list of the events
       suitable for the simulateCheckoutLine function.  Be sure to
       check that the file exists and print an error message and exit
       if not."""

    



    if not os.path.isfile( filename ):
        print("File", filename, "does not exist.")
        return

    infile = open(filename, "r")


    eventlist = []
    line = infile.readline()
    while line:
        evets = line.split()
        for evet in evets:
            eventlist.append(int(evet))
        line = infile.readline()
    infile.close()

    return eventlist
    
            

############################## Customer Class ############################## 

class Customer:

    def __init__(self, custNum, itemCount):
        """A new customer is assigned a customer number and also a number of
        items in their basket."""
    

        self.__num = custNum
        self.__item = itemCount

    def getCustomerNumber(self):
        """Getter for the customer's number."""
        return self.__num

    def getItemsCount(self):
        """Getter for the customer's current count of items."""
        return self.__item 

    def decrementItemsCount(self):
        """Ring up (remove) one item from this customer's basket. 
        Typically, we'll only call this on the first customer in line."""
        self.__item -= 1

    def customerFinished(self):
        """Boolean function indicating that this customer will depart on 
        the current tick, i.e., there are zero items in their basket.  
        Typically we'll only call this on the first customer in line."""
        if self.__item == 0:
            return True
        if self.__item != 0:
            return False

    def __str__(self):
        """If this is customer n with k items in basket,
        return 'Cn(k)' """
        return "C" + str(self.__num) + "(" + str(self.getItemsCount()) + ")"



############################## CheckoutLine Class ############################## 

class CheckoutLine:
    """A checkout line is implemented as a list with customers added at the front
    (L[0]) and removed from the rear (L[-1]).  Customers enter and
    move through the line.  At each tick, one item is removed from the
    basket of the first customer in line.  When their basket becomes
    empty, the first customer departs the line."""

    def __init__(self):
        """ Open a new line, with no customers initially. """

        self.__value = []
    
    def __len__(self):
        """Return the current length of the line."""
        return len(self.__value)

    def firstInLine(self):
        """ Return the first customer in the line."""
        return self.__value[-1]

    def customerJoinsLine(self, cust):
        """ Add a new customer at the rear of the line.  Print a
            message indicating that the customer joined. """
        self.__value.insert(0, cust)
        print("Customer " + str(cust)[:2] + " joining line.")
        
    def customerLeavesLine(self):
        """ The first customer in line departs.  Remove the customer
            from the line and print a message. """

        print("Customer " + str(self.__value[-1])[:2] + " leaving line.")  
        self.__value.pop()
  

    def advanceLine( self ):
        """ If the line is empty, don't change anything.  Otherwise,
            remove one item from the basket of the first customer in
            line.  If their basket becomes empty, they leave the
            line. (Use the previous methods to implement this.)"""
        if self.__value != []:
            custo = self.firstInLine()
            custo.decrementItemsCount()
            if custo.getItemsCount() == 0:
                self.customerLeavesLine()
            

    def __str__(self):
        """ Return a string that shows the current state of the line. """
        newStr = ""
        for i in self.__value:
            newStr += str(i) + " "
        
        return "   Line: " + "[ " + newStr + "]"

############################## Driver for the Simulation ############################## 

# The following function takes a list of events (non-negative integers) and drives
# the simulation based on the items in this list. 

def simulateCheckoutLine( eventList ):

    """This is the driver program for this system.  We monitor the
        progress of customers in the checkout line.  The eventList
        decides when a new customer is added with how many items in
        their cart. Customers are numbered as they enter. At each tick
        of the simulator clock (each new item in eventList), the
        cashier processes one item in the basket of the first
        customer."""

    print("Simulating a simple market, with one Cashier.")
    new = CheckoutLine()
    counter = 0
    countCust = 0
    for i in eventList:
        counter += 1
        print("")
        print("Step:", counter)
        new.advanceLine()
        if i != 0:
            countCust += 1
            custo = Customer(countCust, i)
            new.customerJoinsLine(custo)
        
        print(str(new)) 

