print("Welcome to my Python Program!") # welcome message, this feels so cool im acc professional noww
hours = input("How many hours did you study today? ") # user input for hours studied today
hours = float(hours) # convert input to float for calculation
weekly_hours = hours * 7 # calculates weekly hours based on daily input
print(f"Great! If you study {hours} hours daily, you'll study {weekly_hours} hours this week!") # output weekly hours
try: # error handling for non-numeric input
    hours = float(hours)
except ValueError:
    print("Please enter a valid number for hours studied.") # error message for invalid input
    exit()