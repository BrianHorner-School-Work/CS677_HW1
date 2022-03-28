"""
Brian Horner
CS 677 - Summer 2
Date: 7/11/2021
Print Helper for Homework Problem: 1_1 , 1_2, an 1_3
This program takes the calculations of mean of daily returns, standard
deviation of returns and count of positive and negative returns from the file
functions_helper. It uses these to return a table of results for individual
years or all years of a stock from data provided."""


# Import statements for the print function to use.
from function_helper import count_positive_negative
from function_helper import mean_of_daily_returns, standard_deviation


def table_print(data, ticker, year="All"):
    """Prints the mean, standard deviation for all, positive and negative
    returns, Prints the count for positive and negative returns. Formats
    into a table with the Weekdays and assignment specified header at the
    top. Can specify a specific year, default is all years"""
    weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    header_list = ['Day', 'u(R)', 'o(R)', '|R-|', 'u(R-)', 'o(R-)', '|R+|',
                   'u(R+)', 'o(R+)']
    print_list = []
    # Iterating through weekday list.
    for day in weekday_list:
        # Adding the results of the calculations on the weekday to a temp list
        temp_list = [day, round(mean_of_daily_returns(day, data, year), 2),
                     round(standard_deviation(day, data, year), 2),
                     round(count_positive_negative(day, data, year,
                                                   "Negative"), 2),
                     round(mean_of_daily_returns(day, data, year,
                                                 value='Negative'), 2),
                     round(standard_deviation(day, data, year,
                                              value='Negative'), 2),
                     round(count_positive_negative(day, data, year,
                                                   "Positive"), 2),
                     round(mean_of_daily_returns(day, data, year,
                                                 value='Positive'), 2),
                     round(standard_deviation(day, data, year,
                                              value='Positive'), 2)]
        # Appending weekday temp list to total print list
        print_list.append(temp_list)
    # Inserting the header as the first list in the print list
    print_list.insert(0, list(header_list))
    # Adding descriptive line to indicate which stock and which year or years
    # are being printed.
    if year == 'All':
        print(f"---Table of Stock evaluation of {ticker} for 2015-2020---")
    else:
        print(f"---Table of Stock evaluation of {ticker} for {year}---")
    # Enumerating over print list
    for index, stuff in enumerate(print_list):
        # Adding a | in front of each value of the lists in print list
        row = '|'.join(str(value).ljust(12) for value in stuff)
        # Printing the row for the list in print list
        print(row)
        # Adding a line between the header and the data rows
        if index == 0:
            print('-' * len(row))
    print("\n")

if __name__ == "__main__":
    """Units Tests"""
    pass
