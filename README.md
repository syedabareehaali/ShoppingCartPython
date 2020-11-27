# ShoppingCartPython
PROBLEM DESCRIPTION:
Online shopping cart is a virtual shopping trolley, where shoppers can put all of their
want-to-buy products in, review to make adjustments in quantity, product attributes,
etc., and remove it before or during the checkout if they change their mind.

DISTINGUISHING FEATURES OF PROJECT:
I have added doc-strings in each method and class of my Shopping Cart project to make
my code pleasant and easy to understand. Moreover, there is a private method in the
application that displays personal information (Users’ Password) to the owner of the
Shopping Mart upon inputting the relevant password.
Also, my application exhibits the following object oriented features:
 Exception Handling
 Method Overriding
 Inheritance
 Association


FLOW OF PROJECT:
CLASS Stationery:
Its attribute stationery is a list of dictionary containing Shop items’ information.

CLASS Login:
It verifies the registered user, registers the unregistered customer, maintains records of
all registered users and also displays their shopping history upon customer’s choice.

CLASS DisplayMenu:
It displays the ID, name, availability and price of items of the Shopping Cart.

CLASS Order:
It takes the ID of an item as input from user using while loop and in this way creates list
MyCart having ID of user’s selected items.

CLASS CancelOrder:
It takes item’s ID from user as an input and removes that from his/her cart (list
MyCart). If the input ID is not present in his cart then it prints a relevant message for
this.

CLASS Item:
It displays the total available items that are present in the stock, through its method
shopping_items().

CLASS UserCart:
It displays the user the list of items that he has shopped yet.

CLASS Logout:
Its method, logout(), when called, ends the application.

CLASS UserPersonalInfo:
It displays all the stored information of registered users to the owner after taking
password as input from the owner through the private method
__personalInfo().
