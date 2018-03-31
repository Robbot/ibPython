from datetime import datetime
def main():
    now = datetime.now()
    
  # Times and dates can be formatted using a set of predefined string
  # control codes 

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is %Y"))
    print(now.strftime("The current two last digits of the year is %y"))
    print(now.strftime("The current day short name is %a"))
    print(now.strftime("The current day full name is %A"))
    print(now.strftime("The current month short name is %b"))
    print(now.strftime("The current month full name is %B"))
    print(now.strftime("The current day of month is %d"))
  # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("locale date and time %c"))
    print(now.strftime("locale date %x"))
    print(now.strftime("locale time %X"))

  #### Time Formatting ####
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time in 12h format %I:%M:%S %p"))
    print(now.strftime("Current time in 24h format %H:%M:%S"))
     
main()