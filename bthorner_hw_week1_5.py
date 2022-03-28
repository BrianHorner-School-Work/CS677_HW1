"""
Brian Horner
CS 677 - Summer 2
Date: 7/11/2021
Week 1 Homework Problems: 5
This program calculates the total return of using a buy and hold strategy
with an investment of 5 years for the stocks SPY and HSY.
"""

# Imports:
import csv
import os
from function_helper import following_oracle


spy_ticker = 'SPY'
input_dir = r''
spy_ticker_file = os.path.join(input_dir, spy_ticker + '.csv')

hsy_ticker = 'HSY'
input_dir = r''
hsy_ticker_file = os.path.join(input_dir, hsy_ticker + '.csv')


def buy_and_hold(data):
    """Calculates the total return from a $100 starting investment over
    5 years of the provide stock using a buy and hold strategy. Calculated
    from data provided returns."""
    investment = 100
    for line in data:
        try:
            investment = investment*(1+float(line[13]))
        except ValueError:
            pass
    return round(investment, 2)

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
print("---Output for Homework questions 5 for week 1 of CS 677---")


# Question 5.1
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 5.1 How much money will you have on the last trading day "
      f"of 2020 for each stock (with a buy and hold strategy)?\n")
print(f" With a Buy and Hold Strategy with 'HSY' I would have "
      f"${buy_and_hold(clean_data_hsy)} on the last trading day of 2020.")
print(f" With a Buy and Hold Strategy with 'Spy' I would have "
      f"${buy_and_hold(clean_data_spy)} on the last trading day of 2020.")
# Question 5.2
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 5.2 How do these results compare with the results obtained "
      f"in question 4?\n")
print(f"I would have $"
      f"{following_oracle(clean_data_hsy) - buy_and_hold(clean_data_hsy):,} "
      f"more by following the oracle for the stock 'HSY'")
print(f"I would have $"
      f"{following_oracle(clean_data_spy) - buy_and_hold(clean_data_spy):,} "
      f"more by following the oracle for the stock 'HSY'")
