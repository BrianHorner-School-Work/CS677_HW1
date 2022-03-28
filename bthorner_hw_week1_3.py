"""
Brian Horner
CS 677 - Summer 2
Date: 7/11/2021
Week 1 Homework Problems: 1 and 2
This program calculates of mean of daily returns, standard
deviation of returns and count of positive and negative returns using
functions for the stocks SPY and HSY for the years 2016-2020. It then
returns a table for both. It does this using the print_helper function.
"""

# Imports: print_helper calls function_helper to do calculations
import csv
import os
from print_helper import table_print

spy_ticker = 'SPY'
input_dir = r''
spy_ticker_file = os.path.join(input_dir, spy_ticker + '.csv')

hsy_ticker = 'HSY'
input_dir = r''
hsy_ticker_file = os.path.join(input_dir, hsy_ticker + '.csv')

print("---Output for Homework question 3 for week 1 of CS 677---\n")
try:
    with open(spy_ticker_file) as spy_file:
        # Commented the below line out as it makes the processing harder
        # lines = f.read().splitlines()
        # Using csv.reader we can have a list of lists which we can index
        messy_data = csv.reader(spy_file)
        clean_data_spy = list(messy_data)
        print(f"Opened file for ticker: {spy_ticker}\n")
except Exception as e:
    print(e)
    print(f"Failed to read stock data for ticker: {spy_ticker}")
try:
    with open(hsy_ticker_file) as hsy_file:
        messy_data = csv.reader(hsy_file)
        clean_data_hsy = list(messy_data)
        print(f"Opened file for ticker: {hsy_ticker}\n")
except Exception as e:
    print(e)
    print(f"Failed to read stock data for ticker: {hsy_ticker}")


"""Print statements for questions below"""
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 3 Tables:\n")
table_print(clean_data_spy, 'SPY')
table_print(clean_data_hsy, 'HSY')

# Question 3.1
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 3.1: What is the best and worst days of the week for each?\n")
print(f"The best day for 'SPY' is Tuesday with a mean return of 0.27 and the "
      f"worst day is Thursday with a mean return of -0.03.")
print(f"The best day for 'HSY' is Friday with a mean return of 0.12 and the "
      f"worst days are Monday and Wednesday with mean returns of -0.03.")
print('\n')

# Question 3.2
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 3.2: Are these days the same for your stock as they are for "
      f"S&P 500?\n")
print(f"No the best and worst days for 'HSY' and 'SPY' are not the same.")
