# RESTAURANT_BILLING_SYSTEM

This is a simple billing system application developed using Python and Tkinter. It allows the restaurant staff to take orders, calculate the total bill, and generate a printable bill receipt for the customers.

## Features

- Enter customer details, including name, phone number, and table number.
- Choose items from the menu in three categories: Snacks, Specialties, and Beverages.
- Calculate the total bill, including item-wise prices and taxes.
- View and save the bill with customer details, items purchased, total bill, and timestamp.

## User Interface

![Screenshot (11)](https://github.com/JILSPATEL/restaurant-billing-system/assets/100358865/80eb676a-b2a9-4fe8-8e0f-64b38d598814)

## Usage

1. Enter the customer's name, phone number, and table number.
2. Choose the quantity of items from each category (Snacks, Specialties, and Beverages).
3. Click the "Calculate Bill" button to view the total bill with item-wise prices and taxes.
4. Optionally, click the "View Bill" button to see the complete bill in the "Bill Area."
5. Click the "Save Bill" button to save the bill in a CSV file named `hotel.csv`.
6. Click the "Clear" button to reset the order and customer details.
7. Click the "Exit" button to close the application.

## Data Persistence

The application saves the customer's bill in a CSV file named `hotel.csv`. If the file does not exist, it creates one and writes the data to it. If the file already exists, it appends the new bill data to the existing file.

## Dependencies

- Python 3.x
- tkinter (built-in with Python)
- csv (built-in with Python)
- random (built-in with Python)
- time (built-in with Python)
- tempfile (built-in with Python)
- os (built-in with Python)
- pathlib (built-in with Python)

## Note

This application has a basic implementation and can be further enhanced by adding more features, validation checks, and improvements to the user interface.
