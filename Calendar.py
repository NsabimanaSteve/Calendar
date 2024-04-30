class Calendar:
    def __init__(self,year):
        self.year = year
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def days_in_month(self,month):
        days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self.is_leap_year():
            return 29
        else:
            
            return days_in_month[month-1]
def print_calendar(year):
    cal=Calendar(year)
    months=['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    for month in range(1,13):
        days = cal.days_in_month(month)
        print(f"\n{months[month-1]} {year}")
        print("Mon Tue Wed Thu Fri Sat Sun")
        
        #Calculating the starting day of the week
        start_day=(1+sum(cal.days_in_month(m) for m in range(1, month))) % 7
        
         #Print leading spaces for the first week
        print("    " * start_day, end='')
        
        # Print days of the month
        for day in range(1, days + 1):
            print(f"{day:3}", end=' ')
            start_day += 1
            if start_day == 7:  # Start a new line for the next week
                print()
                start_day = 0
        print()

# Test the function
year = int(input("Enter the year: "))
print_calendar(year)
                