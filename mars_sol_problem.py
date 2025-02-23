def mars(day, month, year):

    # Check for valid Martian date
    if year < 1 or month < 1 or month > 24 or day < 1 or (month % 6 != 0 and day > 28):
        return -1
    
    # Adjust maximum days in month 
    if (year % 2 != 0 or year % 10 == 0): 
        # leap year condition 
        if (month == 24 and day > 28) or (month % 6 == 0 and month != 24 and day > 27) or (month % 6 != 0 and day > 28): 
            return -1 
    else: 
        if (month % 6 == 0 and day > 27) or (month % 6 != 0 and day > 28): 
            return -1

    year_b = 1
    begining_day = 1
    
    # After analysis, I get this formula, And It's work for every year.
    if year>=220:
        begining_day = (5 + year//220 - 1)%7
        year_b = ((year//220)*220)

    # Calculate the beginning day of the given year
    for y in range(year_b, year):
        if y % 2 != 0 or y % 10 == 0:
            no_sol = 669
        else:
            no_sol = 668
            
        begining_day = ((no_sol % 7) + begining_day) % 7

    sols = 0

    # Calculate the total number of sols up to the given month
    for m in range(1, month):
        if m % 6 == 0:
            sols += 27
        else:
            sols += 28
            
    sols += day

    # Return the Martian day of the week
    return (begining_day + sols - 1) % 7
