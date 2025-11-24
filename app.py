print("Welcome to my Python Program!")
hours = input("How many hours did you study today? ")
hours = float(hours)
weekly_hours = hours * 7
print(f"Great! If you study {hours} hours daily, you'll study {weekly_hours} hours this week!")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number for hours studied.")
    exit()