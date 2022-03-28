"""
Brian Horner
CS 677 - Summer 2
Date: 7/11/2021
Week 1 Homework Problems: 1 and 2
This program calculates of mean of daily returns, standard
deviation of returns and count of positive and negative returns using
functions for the stock HSY for the years 2016-2020. It then returns a
table for each year. It does this using the print_helper function.
"""

# Imports: print_helper calls function_helper to do calculations
import csv
import os
from print_helper import table_print
from function_helper import count_positive_negative, mean_of_daily_returns


hsy_ticker = 'HSY'
input_dir = r''
hsy_ticker_file = os.path.join(input_dir, hsy_ticker + '.csv')
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
years = ['2016', '2017', '2018', '2019', '2020']


def total_neg_pos_counter(data):
    """Calculates the total positive return and negative return days between
    2016-2020. Returns information in tailed print statement."""
    total_positive = 0
    total_negative = 0
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    years = ['2016', '2017', '2018', '2019', '2020']
    print(f"---Data for the years 2016-2020---")
    # Iterating through years and weekdays to get every count
    for year in years:
        for weekday in weekdays:
            # Adding counts to totals
            total_positive += count_positive_negative(weekday, data, year,
                                                      value='Positive')
            total_negative += count_positive_negative(weekday, data, year,
                                                      value='Negative')
    # Comparison for tailored print statement
    if total_positive > total_negative:
        return f"There are more positive returns {total_positive} than " \
                f"negative returns {total_negative} for HSY in the years " \
                f"2016-2020.\n"
    else:
        return f"There are more negative returns {total_negative} than " \
                f"positive returns {total_positive} for HSY in years " \
                f"2016-2020.\n"


def year_neg_pos_counter(data, year):
    """Calculates the total positive and negative return days for a given
    year. Returns information in a tailored print statement."""
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(f"---Data for the year {year} below---")
    total_positive = 0
    total_negative = 0
    for weekday in weekdays:
        # Grabbing total positive and negative for each weekday in year
        total_positive += count_positive_negative(weekday, data, year=year,
                                                  value='Positive')
        total_negative += count_positive_negative(weekday, data, year=year,
                                                  value='Negative')
    # Comparison for tailored print statement
    if total_positive <= total_negative:
        return f"There are more negative returns {total_negative} than " \
                f"positive returns {total_positive} for HSY the year {year}.\n"
    else:
        return f"There are more positive returns {total_positive} than " \
               f"negative returns {total_negative} for HSY in the year " \
               f"{year}.\n"


def total_loss_gain_calc(data):
    """Calculates the total mean of all positive and negative returns to
    determine if a stock lost or gained more on average. Returns information
    in tailored print statement."""
    total_positive_returns = 0
    total_negative_returns = 0
    count = 0
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(f"---Data between 2016-2020 below---")
    for weekday in weekdays:
        # Adding weekday positive returns to total returns
        total_positive_returns += mean_of_daily_returns(weekday, data,
                                                        value='Positive')
        # Adding weekday negative returns to total returns
        total_negative_returns += mean_of_daily_returns(weekday, data,
                                                        value='Negative')
        count += 1
    # Calculating the mean of all positive and negative returns
    mean_total_positive_returns = total_positive_returns/count
    mean_total_negative_returns = total_negative_returns/count
    # Comparison to return a tailored print statement
    if mean_total_positive_returns > abs(mean_total_negative_returns):
        return f"HSY gained more on a up day (" \
               f"{round(mean_total_positive_returns,2)}) than it " \
               f"lost on a down day (" \
               f"{round(mean_total_negative_returns,2)}) on average for the " \
               f"years 2016-2020.\n"
    else:
        return f"HSY lost more on a down day (" \
               f"{round(mean_total_negative_returns,2)}) " \
               f"than it gained on a up day (" \
               f"{round(mean_total_positive_returns,2)}) on average for the " \
               f"years 2016-2020.\n"


def year_loss_gain_calc(data, year):
    """Calculates the total loss and gain mean for all days in the provided
    year. It returns this information in a tailored print statement"""
    total_positive_returns = 0
    total_negative_returns = 0
    count = 0
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    # Iterating through all weekday
    for weekday in weekdays:
        # Grabbing mean of daily positive returns for each weekday and adding
        # to total
        total_positive_returns += mean_of_daily_returns(weekday, data,
                                                        year=year,
                                                        value='Positive')
        # Grabbing mean of daily positive returns for each weekday and adding
        # to total
        total_negative_returns += mean_of_daily_returns(weekday, data,
                                                        year=year,
                                                        value='Negative')
        count += 1
    # Calculating the mean of all positive and negative returns in a year
    mean_total_positive_returns = total_positive_returns/count
    mean_total_negative_returns = total_negative_returns/count
    # Comparison of means for correct print statement
    if mean_total_positive_returns > abs(mean_total_negative_returns):
        return f"HSY gained more on a up day (" \
                f"{round(mean_total_positive_returns,2)}) than it " \
                f"lost on a down day (" \
                f"{round(mean_total_negative_returns,2)}) on average for the " \
                f"year {year}."
    else:
        return f"HSY lost more on a down day (" \
                f"{round(mean_total_negative_returns,2)}) " \
                f"than it gained on a up day (" \
                f"{round(mean_total_positive_returns,2)}) on average for " \
                f"the year {year}."


def weekday_loss_gain_calc(data, weekday):
    """Calculates the total loss and gain for a weekday
    between the years 2016-2020. It returns this information in a tailored
    print statement."""
    # Grabbing positive returns for weekday in the years 2016-2020
    mean_positive = mean_of_daily_returns(weekday, data, value='Positive')
    # Grabbing negative returns for weekday in years 2016-2020
    mean_negative = mean_of_daily_returns(weekday, data, value='Negative')
    # Comparison of means for correct print statement based on which is greater
    if mean_positive > abs(mean_negative):
        return f"HSY gained more on a up day (" \
               f"{round(mean_positive,2)}) than it " \
               f"lost on a down day (" \
               f"{round(mean_negative,2)}) on average on " \
               f"{weekday}'s from 2016-2020"
    else:
        return f"HSY lost more on a down day (" \
               f"{round(mean_negative,2)}) " \
               f"than it gained on a up day (" \
               f"{round(mean_positive,2)}) on average on " \
              f"{weekday}'s from 2016-2020."


def weekday_and_year_loss_gain_calc(data, year, weekday):
    """Calculates the total loss and gain for a weekday in a year.
    It returns this information in a tailored print statement for
    user"""
    # Grabbing positive mean return
    mean_positive = mean_of_daily_returns(weekday, data, year, value='Positive')
    # Grabbing negative mean return
    mean_negative = mean_of_daily_returns(weekday, data, year, value='Negative')
    # Comparison for correct print statements based on which is greater
    if mean_positive > abs(mean_negative):
        return f"HSY gained more on a up day (" \
               f"{round(mean_positive,2)}) than it " \
               f"lost on a down day (" \
               f"{round(mean_negative,2)}) on average on " \
               f"{weekday}'s in {year}."
    else:
        return f"HSY lost more on a down day (" \
               f"{round(mean_negative,2)}) " \
               f"than it gained on a up day (" \
               f"{round(mean_positive,2)}) on average on " \
              f"{weekday}'s in {year}."


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


print("---Output for Homework questions 1 and 2 for week 1 of CS 677---\n")
for year in years:
    table_print(clean_data_hsy, 'HSY', year)


# Question 1.3
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 1.3: Are there more negative or non-negative returns?\n")
print(total_neg_pos_counter(clean_data_hsy))
for year in years:
    print(year_neg_pos_counter(clean_data_hsy, year))
print("\n")


# Question 1.4
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 1.4: Does your stock lose more on a 'down' day than it "
      f"gains on an 'up' day?\n")
print(total_loss_gain_calc(clean_data_hsy))
print(f"Loss and gain comparison for the years 2016-2020 individually.")
for year in years:
    print(year_loss_gain_calc(clean_data_hsy, year))
print('\n')


# Question 1.5
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 1.5: Are these results the same across days of the "
      f"week?\n")
print(f"\n --- Loss and gain comparison for weekday's between 2016-2020 below")
for weekday in weekdays:
    print(weekday_loss_gain_calc(clean_data_hsy, weekday))

for year in years:
    print(f'\n---Loss and gain comparison for {year} below ---')
    for weekday in weekdays:
        print(weekday_and_year_loss_gain_calc(clean_data_hsy, year, weekday))


# Question 2.1
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 2.1 Are there any patterns across days of the week?\n")
print(f"It seems that at least once a week there is a string of two days with "
      f" mean returns of a loss. "
      f"2016 - Tuesday, Wednesday\n2017 - Thursday, Friday\n"
      f"2018 - Wednesday, Thursday\n2019 - Thursday, Friday\n2020 - Thursday, "
      f"Friday")
# Question 2.2
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 2.2 Are there any patterns across different years for the "
      f"same day of the week?\n")
print(f"Mondays has a loss of return of -1.0 for all years in 2017-2020. "
      f"Tuesday has a gain every year except 2016. Thursday has a loss in "
      f"every year except 2016.")

# Question 2.3
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 2.3 What are the best and worst days of the week to invest "
      f"for each year?\n")
print(f"The best day of the week to invest is Tuesday with a gain every year "
      f"except 2016. The mean of gains is 1.21 with a total mean return of "
      f"0.76")
print(f"The worst day of the week to invest is Thursday with a mean loss of "
      f"-1.415 for the years 2017-2020 and a mean return of 0.1. Although "
      f"question three shows that worst days are Monday and Wednesday "
      f"with mean returns of -0.03. ")

# Question 2.4
print(f"\n------------------------------------------------------------------"
      "--------------------------------------------------------------------")
print(f"Question 2.4 Do these days change from year to year?\n")
print(f"Yes the best and worst days change year to year, see below:")
print(f"2016 - Best: Thursday, Worst: Tuesday\n")
print(f"2017 - Best: Tuesday, Worst: Thursday\n")
print(f"2018 - Best: Friday, Worst: Monday\n")
print(f"2019 - Best: Wednesday, Worst: Thursday\n")
print(f"2020 - Best: Tuesday, Worst: Wednesday\n")

