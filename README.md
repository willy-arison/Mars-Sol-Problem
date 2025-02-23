### Mars Sol Problem: Calculating the Day of the Week on Mars

#### Description
This project calculates the day of the week on Mars for a given date in the Martian calendar. The Martian calendar has 24 months, with most months having 28 days and the 6th, 12th, 18th, and 24th months having 27 days. Leap years on Mars occur when the year is odd or divisible by 10, adding an extra day to the 24th month.

The function `mars(day, month, year)` calculates the day of the week (0-6) for a given Martian date, where:
- `0` represents Sunday
- `1` represents Monday
- ...
- `6` represents Saturday

If the input date is invalid, the function returns `-1`.

#### Key Features
- **Martian Calendar Rules:** Handles the unique structure of the Martian calendar, including leap years.
- **Efficient Calculation:** Computes the day of the week using modular arithmetic and iterative calculations.
- **Input Validation:** Ensures the input date is valid according to Martian calendar rules.
