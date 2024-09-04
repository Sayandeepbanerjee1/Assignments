month_to_season = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Fall',
    10: 'Fall', 11: 'Fall', 12: 'Winter'
}
# Function to get season by month number
def get_season_by_month(month):
    if 1 <= month <= 12:
        return month_to_season[month]
    else:
        return "Invalid month number"
# Get user input for month number
try:
    month = int(input("Enter the month number (1-12): "))
    season = get_season_by_month(month)
    print(f"The season for month {month} is {season}.")
except ValueError:
    print("Invalid input. Please enter a valid number between 1 and 12.")
