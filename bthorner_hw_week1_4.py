"""
Brian Horner
CS 677 - Summer 2
Date: 7/11/2021
Week 1 Homework Problems: 4
This program calculates calculates the total return for a $100 dollar
investment for the stocks SPY and HSY if an oracle that helps you
avoid negative return days is used.
"""

# Imports
import csv
import os
from function_helper import following_oracle

spy_ticker = 'SPY'
input_dir = r''
spy_ticker_file = os.path.join(input_dir, spy_ticker + '.csv')

hsy_ticker = 'HSY'
input_dir = r''
hsy_ticker_file = os.path.join(input_dir, hsy_ticker + '.csv')

print("---Output for Homework question 4 for week 1 of CS 677---\n")
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

"""Question answers below"""
print("---Output for Homework questions 4 week 1 of CS 677---\n")
print(f"Question 4.1: How much money will you have on the last trading day "
      f"following the oracle for HSY?")
# Oracle function call for HSY
print(f"I would have ${(following_oracle(clean_data_hsy)):,.2f} on the last "
      f"trading day of 2020 if I followed the oracle for HSY.\n")
print(f"Question 4.2: How much money will you have on the last trading day "
      f"following the oracle for SPY?")
# Oracle function call for SPY
print(f"I would have ${(following_oracle(clean_data_spy)):,.2f} on the last "
      f"trading day of 2020 if I followed the oracle for SPY.\n")
