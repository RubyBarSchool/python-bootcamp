#Solution 1
def is_leap_year(year):
    """
    Returns True if the given year is a leap year, otherwise False.
    A leap year is divisible by 4, but not by 100 unless also divisible by 400.
    """
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False
#Solution 2
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#Solution 3
import calendar
def is_leap_year(year):
    return calendar.isleap(year)