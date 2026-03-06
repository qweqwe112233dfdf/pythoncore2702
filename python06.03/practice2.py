def leap_year(year):
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def month_days(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return 31
    
def date(day, month, year):
    total_days = 0
    for y in range(1, year):
        total_days += 366 if leap_year(y) else 365
        