from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print("Today's date is ",today)
    print("Date's components ", today.day, today.month, today.year)
    print("Today's # weekday number is ", today.weekday())
    days =["mon","tue","wed","thu","fri","sat","sun"]
    print("which is a",days[today.weekday()])
    # another section datetime
    today1 = datetime.now()
    print("The current time is",today1)
    t=datetime.time(datetime.now())
    print(t)
main()