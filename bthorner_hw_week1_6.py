"""
Brian Horner
CS 677 - Summer 2
Date: 7/11/2021
Week 1 Homework Problems: 6
This program calculates calculates the total return for a $100 dollar
investment for the stocks SPY and HSY if an oracle gets mad at you. The
oracle will exclude the 10 best trading days, include the worst 10 days
and exclude the 5 best trading days and include the 5 worst trading days.
We do these in functions called mad_oracle_best, mad_oracle_worst,
and mad_oracle_both.
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


def mad_oracle_best(data):
    """Calculates the total return from a $100 starting investment over
    5 years of the provided stock using the oracle to miss all negative
    return days. Oracle also excluded top ten return days in spite of the
    user. Calculated from data provided returns."""
    investment = 100
    return_list = []
    for line in data:
        try:
            if float(line[13]) >= 0:
                return_list.append(float(line[13]))
        except ValueError:
            pass
    return_list.sort(reverse=True)
    return_list_clean = return_list[10:]
    for item in return_list_clean:
        investment = investment*(1+float(item))
    return round(investment,2)


def mad_oracle_worst(data):
    """Calculates the total return from a $100 starting investment over
    5 years of the provided stock using the oracle to miss negative
    return days. Oracle includes worst ten return days in spite of the
    user. Calculated from data provided returns."""
    investment = 100
    negative_returns = []
    for line in data:
        try:
            if float(line[13]) >= 0:
                investment = investment*(1+float(line[13]))
            elif float(line[13]) < 0:
                negative_returns.append(float(line[13]))
        except ValueError:
            pass
    negative_returns.sort()
    missed_negative_returns = negative_returns[:10]
    for item in missed_negative_returns:
        investment = investment*(1+float(item))
    return round(investment,2)


def mad_oracle_both(data):
    """Calculates the total return from a $100 starting investment over 5
    years of the provided stock using the oracle to miss negative returns
    days. Oracle includes worst 5 return days and excludes top 5 return days
    in spite of the user. Calculated from data provided returns."""
    investment = 100
    positive_returns = []
    negative_returns = []
    for line in data:
        try:
            if float(line[13]) >= 0:
                positive_returns.append(float(line[13]))
            elif float(line[13]) < 0:
                negative_returns.append(float(line[13]))
        except ValueError:
            pass
    positive_returns.sort(reverse=True)
    negative_returns.sort()
    missed_negative_returns = negative_returns[:5]
    missed_positive_returns = positive_returns[:5]
    for item in positive_returns:
        if item not in missed_positive_returns:
            investment = investment*(1+float(item))
    for item in missed_negative_returns:
        investment = investment*(1+float(item))
    return round(investment, 2)


print("---Output for Homework question 6 for week 1 of CS 677---\n")
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
# Question 6.1
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 6.1: Compute each oracle output.\n")

# SPY Oracle print statements and function calls

print(f"Final total of $100 investment with oracle "
      f"missing the best 10 return days ${mad_oracle_best(clean_data_spy)} "
      f"for the stock 'SPY'.")

print(f"Final total of $100 investment with oracle "
      f"missing the worst 10 return days ${mad_oracle_worst(clean_data_spy)} "
      f"for the stock 'SPY'.")

print(f"Final total of $100 investment with oracle "
      f"missing the 5 best return days and 5 worst return days is"
      f" ${mad_oracle_both(clean_data_spy)} for the stock 'SPY'")

print("")
# HSY Oracle print statements and function calls

print(f"Final total of $100 investment with oracle "
      f"missing the best 10 return "
      f"days ${mad_oracle_best(clean_data_hsy)} for the stock 'HSY'.")

print(f"Final total of $100 investment with oracle "
      f"missing the worst 10 return "
      f"days ${mad_oracle_worst(clean_data_hsy)} for the stock 'HSY'.")

print(f"Final total of $100 investment with oracle "
      f"missing the 5 best return days and 5 worst return days is"
      f" ${mad_oracle_both(clean_data_hsy)} for the stock 'HSY'")

# Question 6.2
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 6.2: Do you gain more by missing the worst days or by missing "
      f"the best days?\n")
print(f"You are better to miss the top 10 best return days for the stocks. "
      f"\nBelow is the calculation of how much the difference between missing "
      f"the top 10 return days and worst 10 return days for each stock.\n")

print(f"You would make $"
      f"{mad_oracle_best(clean_data_spy) - mad_oracle_worst(clean_data_spy):,.2f}"
      f" more by missing the 10 best return days instead of the 10 worst for "
      f"the stock 'SPY'.")
print(f"You would make $"
      f"{mad_oracle_best(clean_data_hsy) - mad_oracle_worst(clean_data_hsy):,.2f}"
      f" more by missing the 10 best return days instead of the 10 worst for "
      f"the stock 'SPY'.")

# Question 6.3
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 6: Are the results of the oracle missing the best 5 days "
      f"and the worst 5 days different from results obtained in question 4?\n")

print(f"Yes the difference between the oracle working correct or the oracle "
      f"missing best and worst 5 days is huge. Below see the amount of money "
      f"lost by the oracle missing those days.")

print(f"You lost $"
      f"{following_oracle(clean_data_spy)-mad_oracle_both(clean_data_spy):,.2f}"
      f" when the oracle gave you the wrong results for the best 5 days and "
      f"worst 5 days for the stock 'SPY'.")

print(f"You lost $"
      f"{following_oracle(clean_data_hsy)-mad_oracle_both(clean_data_hsy):,.2f}"
      f" when the oracle gave you the wrong results for the best 5 days and "
      f"worst 5 days for the stock 'HSY'.")
