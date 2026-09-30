# General Store Management Software

## Overview

This project is a simple command-line based management program for a general store. It is written in Python and is designed to handle basic billing and sales-history tasks.

The program starts with a main menu where the user can:
- Start a new bill
- Check the sales history
- Exit the program

During billing, the user selects products using product codes. The selected product is added to the current bill and its price is included in the total. The program also keeps track of how many times each product has been sold.

## Features

### 1. Main Menu
The main menu controls the overall flow of the program and gives the user three choices:
- `0` - Start billing
- `1` - Check history
- `2` - Exit

### 2. Billing
The billing module displays the available products, their codes and prices. The user can add more than one product to the same bill and then checkout.

### 3. Sales History
The history option displays:
- Quantity sold for each product
- The total amount of each completed bill during the current program run

## Product List

| Code | Product | Price |
|---:|---|---:|
| 1 | Milk | ₹70 |
| 2 | Cheese | ₹150 |
| 3 | Butter | ₹60 |
| 4 | Chocolate | ₹20 |
| 5 | Juice | ₹30 |
| 6 | Chips | ₹10 |
| 7 | Biscuits | ₹10 |
| 8 | Maggie | ₹15 |
| 9 | Coffee | ₹50 |

## Technologies Used

- Python 3
- Lists
- Functions
- Loops
- Conditional statements
- User input and console output

No external Python libraries are required.

## How to Run

1. Install Python 3 on the computer.
2. Download or clone the project files.
3. Open a terminal/command prompt in the project folder.
4. Run:

```bash
python "VItyarthi project.py"
```

If your system uses `python3`, use:

```bash
python3 "VItyarthi project.py"
```

## How to Use

After starting the program:

1. Select `0` from the main menu to start billing.
2. Choose a product by entering its code.
3. Enter `0` when you want to add another product.
4. Enter `1` when you want to checkout.
5. The final bill amount is displayed and saved in the current session's history.
6. Select `1` from the main menu to view sales history.
7. Select `2` to exit.

## Testing

The program was tested using normal billing operations, including:
- Starting a bill
- Adding multiple products
- Checking the running total
- Completing a bill
- Viewing product quantities sold
- Viewing completed bill totals
- Entering invalid menu/product codes

The current version expects numeric input. Non-numeric input such as letters will raise a Python input conversion error, which is a known limitation and can be improved in a future version.

## Project Structure

At present, the project is intentionally kept as a single Python source file for simplicity:

```text
VItyarthi-Project/
├── VItyarthi project Shubh.py
├── README.md
└── statement.md
```

The submission guideline mentions a 5–10 meaningful module/class/file expectation for coding projects. This version does not fully meet that modularity recommendation because the implementation is contained in one Python file. A future version can separate billing, history, product data, validation and the user interface into individual modules.

## Limitations

- Data is stored only while the program is running.
- There is no database or permanent file storage.
- Product prices are fixed in the source code.
- The program is command-line based.
- Non-numeric user input is not currently handled.

## Future Improvements

Possible improvements include:
- Adding file or database storage
- Adding product stock management
- Adding quantity input directly instead of selecting the same product repeatedly
- Adding customer details and bill numbers
- Adding a graphical user interface
- Adding stronger input validation
- Splitting the program into multiple Python modules
- Adding automated tests

## Author

**Shivam Haritash**  
**Registration No.: 26MIM10146**  

B.Tech First Year — Python Project
