# AUTOMATIZATION REGISTER SALES

Sales Registration Program Documentation
What this program does
This program helps register product sales. You can enter many products and the program will calculate the total value of all sales.

How it works
Step 1: Import functions

from totalventa import totalcalculation - brings a function that calculates the total price of one sale

from historialventa import historial_sales - brings a function that shows all sales information

Step 2: The main function - registerventas()

The program asks you to enter information for each product:

Product name - cannot be empty and cannot be only numbers

Price - must be a positive number

Amount - must be a positive number

The program saves each sale in a dictionary called sales.

Step 3: Continue or finish

After each product, the program asks: "Do you want to enter another sale?"

Press 1 for Yes - you can enter more products

Press 2 for No - the program shows all sales information and total

Step 4: Show results

When you finish, the program:

Shows a list of all products you entered

Shows the total value of all sales

Variables used
is_true - controls the main loop (True = continue, False = stop)

counter - counts how many products you entered

sales - a dictionary that stores all product information

values - adds up the total of all sales

product_bol, price_bol, amount_bol - control loops for user input

individual_sale - the total for one product (amount × price)

Error messages
The program checks for mistakes:

"Error: the name to product only cant numbers" - when product name is only numbers

"Error: the name of the product cant empty" - when product name is empty

"Error: the price to product is only positive" - when price is zero or negative

"Error: the quantity is only positive" - when amount is zero or negative

"Error: please enter a valide number" - when you don't type a number

"No validated" - when you choose a number that is not 1 or 2

"plesae write a num" - when you don't type a number for the menu