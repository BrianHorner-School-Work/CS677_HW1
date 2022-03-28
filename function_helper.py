"""
Brian Horner
CS 677 - Summer 2
Date: 7/11/2021
Function Helper for Homework Problems:  Week 1 Problems 1-6
This program provides the functions to calculate the daily returns,
counts of positive and negative return days, mean of daily returns,
and standard deviation of returns of a weekday. Functions can be used for a
specific year or all. Some functions have specifiers for Positive, Negative,
Zero or All returns.
"""

# Importing square root function from math module
from math import sqrt
# Unit test imports
import csv
import os


def calculate_daily_returns(weekday, data, year='All'):
    """Calculates the daily returns of a stock for the provided weekday.
    Using the adjusted close of a day minus the previous adjusted close to
    calculate. Calculates this by taking the days adjusted close and
    subtracting the
    previous days adjusted close. Can be specified for a specific year,
    else will do for all years included in stock data provided."""
    # List used to hold all calculated returns
    total_returns = []
    # Block for if year is not specified or if it is specified as all
    if year == 'All':
        for line in data:
            if weekday in line:
                try:
                    # Grabbing the days adjusted close
                    days_close = float(line[12])
                    # Grabbing the previous days index
                    previous_index = data.index(line) - 1
                    # Grabbing the previous days adjusted close
                    previous_close = float(data[previous_index][12])
                    # Calculating the return of the day
                    return_of_day = days_close - previous_close
                    total_returns.append(return_of_day)
                    """Passes error when the first adjusted close is 
                        attempted to be subtracted by the header of 'Adj 
                        Close' as string"""
                except ValueError:
                    pass

        return total_returns
    # Code same as above but for a specific year
    elif year != 'All':
        for line in data:
            # Year specifier here. If Row does not contain year pass
            if year in line:
                if weekday in line:
                    try:
                        days_close = float(line[12])
                        previous_index = data.index(line) - 1
                        previous_close = float(data[previous_index][12])
                        return_of_day = days_close - previous_close
                        total_returns.append(return_of_day)
                        """Passes error when the first adjusted close is 
                        attempted to be subtracted by the header of 'Adj 
                        Close' as string"""
                    except ValueError:
                        pass
        return total_returns
    # Catch for in case user submits an invalid year
    else:
        return f"Error your year input of {year} is not valid for " \
               f"computations. You can either enter a year from 2015-2020 in " \
               f"a string or nothing at all for all years."


def count_positive_negative(weekday, data, year='All', value='Total'):
    """Calculates the total number of positive and negative return days for a
    weekday using the calculate_daily_returns function. Can be done for a
    specific year, default is all years. Can be specified to return the counts
    for Positive, Negative or Zero returns, default is all."""

    # Block for if value argument is Positive
    if value == "Positive":
        returns = [value for value in calculate_daily_returns(weekday, data,
                                                              year) if
                   value > 0]
        return len(returns)
    # Block for if value argument
    elif value == 'Negative':
        returns = [value for value in calculate_daily_returns(weekday, data,
                                                              year) if
                   value < 0]
        return len(returns)
    # Block for if value argument is Zeros
    elif value == 'Zeros':
        returns = [value for value in calculate_daily_returns(weekday, data,
                                                              year) if
                   value == 0]
        return len(returns)
    # Block for if value argument is Total
    elif value == 'Total':
        returns = calculate_daily_returns(weekday, data, year)
        return len(returns)
    # Catch for invalid input
    else:
        print(f"Error: Your input of {value} is invalid for this function. "
              f"Valid inputs include 'Positive', 'Negative, 'Zeros' or no "
              f"input")


def mean_of_daily_returns(weekday, data, year='All', value='Total'):
    """Calculates the mean of daily returns for a weekday. Uses
    calculate_daily_returns. Can be specified for a individual year, default
    is all. Can be specified for positive, negative, or zeros, default is
    all."""
    total_return = 0

    # Block for if value argument is Positive
    if value == "Positive":
         # Grabbing all returns that are positive
        returns = [value for value in calculate_daily_returns(weekday, data,
                                                                  year) if
                   value > 0]
        # Iterating over returns
        for item in returns:
            total_return += item
        # Calculating mean of positive returns
        return total_return / len(returns)
    # Block for if value argument is Negative
    elif value == "Negative":
        # Grabbing all returns that are negative
        returns = [value for value in calculate_daily_returns(weekday, data,
                                                                  year) if
                   value < 0]
        # iterating over returns
        for item in returns:
            total_return += item
            # Calculating mean of negative returns
        return total_return / len(returns)
    # Block for if value argument is Zeros
    elif value == "Zeros":
         # Grabbing all returns that are equal to zero
        returns = [value for value in calculate_daily_returns(weekday, data,
                                                                  year) if
                   value == 0]
        count = len(returns)
        # Catch for if there are no days with zero return
        if count == 0:
            return f"Error: You do not have any {weekday}'s in the {year} " \
                   f"with Zero as a return on investment."
        else:
            # Returning zero as the mean of zero returns is always 0
            return 0
        # Block for if value argument is Total or is not included
    elif value == "Total":
        # Grabbing all returns
        returns = calculate_daily_returns(weekday, data, year)
        # Iterating over returns
        for item in returns:
            total_return += item
            # Calculating mean of daily returns
        return total_return / len(returns)
    # Catch for invalid input
    else:
        print(f"Error: Your input of {value} is not valid for the "
                f"mean_of_daily_returns value argument."
                f"Valid inputs include 'Positive', 'Negative, 'Zeros' or no "
                f"input")


def standard_deviation(weekday, data, year="All", value='Total'):
    """Calculates the standard deviation for returns of a weekday using
    mean_of_daily_returns. Can be specified for a specific year, default is
    all.Can be specified for Positive, Negative or Zeros, default is all."""
    total_standard_dev_mean = 0
    # Block for if value argument is Total or not provided
    if value == "Total":
        # Grabbing all returns
        returns = calculate_daily_returns(weekday, data, year)
        # Iterating over returns
        for item in returns:
            # Calculating the numerator for standard deviation formula
            total_standard_dev_mean += (item - mean_of_daily_returns(weekday,
                                                                     data,
                                                                     year,
                                                                     value='Total')) \
                                       ** 2
        # Calculating and returning standard deviation
        return sqrt(total_standard_dev_mean / len(returns))
    # Block for if value argument is Positive
    elif value == "Positive":
        # Grabbing all positive returns
        returns = [value for value in (calculate_daily_returns(weekday, data,
                                                               year)) if value
                   > 0]
        # Iterating over returns
        for item in returns:
            # Calculating the numerator for standard deviation formula
            total_standard_dev_mean += (item - mean_of_daily_returns(weekday,
                                                                     data,
                                                                     year,
                                                                     value='Positive')) ** 2
        # Calculating and returning standard deviation
        return sqrt(total_standard_dev_mean / len(returns))
    # Block for if value argument is Negative
    elif value == "Negative":
        # Grabbing all negative returns
        returns = [value for value in (calculate_daily_returns(weekday, data,
                                                               year)) if
                   value < 0]
        # Iterating over returns
        for item in returns:
            # Calculating the numerator for standard deviation formula
            total_standard_dev_mean += (item - mean_of_daily_returns(weekday,
                                                                     data,
                                                                     year,
                                                                     value='Negative')) ** 2
            # Calculating and returning standard deviation
        return sqrt(total_standard_dev_mean / len(returns))
    # Block for if value argument is Zeros
    elif value == "Zeros":
        returns = [value for value in (calculate_daily_returns(weekday, data,
                                                               year)) if value
                   == 0]
        # Catch for if there are no zero returns
        if len(returns) == 0:
            print(f"Error: You have no zero return days for {weekday}'s in "
                  f"{year}.")
        else:
            # Standard deviation fo zero returns will always be 0
            return 0
    # Catch for if value argument is not valid.
    else:
        print(f"Error: Your input of {value} is not valid for the "
              f"standard_deviation value argument."
              f"Valid inputs include 'Positive', 'Negative, 'Zeros' or no "
              f"input")


def following_oracle(data):
    """Calculates the total return from a $100 starting investment using
    the oracle to miss any negative return days. Calculated from data
    provided returns."""
    investment = 100
    for line in data:
        try:
            # If return of the day is positive use in calculation
            if float(line[13]) >= 0:
                # Recursive calculation of total return
                investment = (investment*(
                    1+float(line[13])))
            # Pass if return is not positive, aka listen to oracle
            else:
                pass
            # ValueError pass for the header of the data
        except ValueError:
            pass
    return round(investment, 2)


if __name__ == "__main__":

    hsy_ticker = 'HSY'
    input_dir = r''
    hsy_ticker_file = os.path.join(input_dir, hsy_ticker + '.csv')
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    years = ['2016', '2017', '2018', '2019', '2020']
    try:
        with open(hsy_ticker_file) as hsy_file:
            # Commented the below line out as it makes the processing harder
            # lines = f.read().splitlines()
            # Using csv.reader we can have a list of lists which we can index
            messy_data = csv.reader(hsy_file)
            clean_data_hsy = list(messy_data)
        print(f"Opened file for ticker: {hsy_ticker}\n")

    except Exception as e:
        print(e)
        print(f"Failed to read stock data for ticker: {hsy_ticker}")


