#  **AUTOMATIZATION REGISTER SALES**

## **Sales Registration Program Documentation**

---

## **What this program does**

This program helps **register product sales**. You can enter many products and the program will calculate the **total value** of all sales.

---

##  **How it works**

###  **Step 1: Import functions**

 Brings a function that **calculates the total price** of one sale
  Brings a function that **shows all sales information**

---

###  **Step 2: The main function - `registerventas()`**

The program asks you to enter information for **each product**:

| Field | Requirement |
|:------|:------------|
|  **Product name** | Cannot be empty and cannot be only numbers |
|  **Price** | Must be a **positive** number |
|  **Amount** | Must be a **positive** number |

The program saves each sale in a dictionary called **`sales`**.

---

###  **Step 3: Continue or finish**

After each product, the program asks:

| Option | Action |
|:-------|:-------|
| **1** |  You can **enter more products** |
| **2** |  The program **shows all sales information and total** |

---

###  **Step 4: Show results**

When you finish, the program:

 Shows a **list of all products** you entered  
 Shows the **total value** of all sales

---

##  **Variables used**

| Variable | Description |
|:---------|:-------------|
| `is_true` | Controls the main loop (`True` = continue, `False` = stop) |
| `counter` | Counts how many products you entered |
| `sales` | A dictionary that stores all product information |
| `values` | Adds up the total of all sales |
| `product_bol` | Controls loop for product name input |
| `price_bol` | Controls loop for price input |
| `amount_bol` | Controls loop for amount input |
| `individual_sale` | The total for one product (amount × price) |

---

##  **Error messages**

The program checks for mistakes:

| Error Message | When it appears |
|:---------------|:-----------------|
| `"Error: the name to product only cant numbers"` | When product name is **only numbers** |
| `"Error: the name of the product cant empty"` | When product name is **empty** |
| `"Error: the price to product is only positive"` | When price is **zero or negative** |
| `"Error: the quantity is only positive"` | When amount is **zero or negative** |
| `"Error: please enter a valide number"` | When you don't type a **number** |
| `"No validated"` | When you choose a number that is **not 1 or 2** |
| `"plesae write a num"` | When you don't type a number for the **menu** |

---

##  **Summary**

This program makes it **easy to register sales** by:

| # | Feature |
|:--|:--------|
| 1️ |  **Validating** all user inputs |
| 2️ |  **Storing** information in an organized way |
| 3️ |  **Calculating** totals automatically |
| 4️ |  **Showing** a complete sales history |

---

>  **Ready to use!** Just run the function `registerventas()` and start registering your sales.

---
