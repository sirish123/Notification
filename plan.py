import time
import datetime
import pytz
import calendar
from datetime import datetime
from datetime import date
from plyer import notification


print("The pomodoro timer has started, start working!")

if __name__ == "__main__":
    while True:
        #info on date and day----
        my_date = date.today() 
        todaysdate= my_date
        workingday=calendar.day_name[my_date.weekday()]
        listdays=["Monday","Tuesday","Wednesday","Thursday","Friday"]
        #info on date and day----

        #info on time and convert to IST----
        tz_NY = pytz.timezone('Asia/Kolkata')    
        now = datetime.now(tz_NY) 
        current_time = now.strftime("%H:%M:%S")
        #info on time and convert to IST----
        if workingday==listdays[0]:
            if current_time>"8:59:50" and current_time<"9:00:00":
                count=0;
                while(count!=1):
                    time.sleep(5)
                    count+=1
                    notification.notify(
                    title = "TIME TABLE!",
                    message =  "BEE"+" SWAPNIL SIR",
                    app_icon = "calendar_clock_schedule_icon-icons.com_51085.ico",
                )
            if current_time>"9:59:50" and current_time<"10:00:00":
                count=0;
                while(count!=1):
                    time.sleep(5)
                    count+=1
                    notification.notify(
                    title = "TIME TABLE!",
                    message =  "SOM"+" VENKAT RAMAN P",
                    app_icon = "calendar_clock_schedule_icon-icons.com_51085.ico",
                )
            if current_time>"10:59:50" and current_time<"11:00:00":
                count=0;
                while(count!=1):
                    time.sleep(5)
                    count+=1
                    notification.notify(
                    title = "TIME TABLE!",
                    message =  "Thermodynamics"+"ANIL KUMAR E",
                    app_icon = "calendar_clock_schedule_icon-icons.com_51085.ico",
                )
            if current_time>"11:59:50" and current_time<"12:00:00":
                count=0;
                while(count!=1):
                    time.sleep(5)
                    count+=1
                    notification.notify(
                    title = "TIME TABLE!",
                    message =  "BEE"+" SWAPNIL SIR",
                    app_icon = "calendar_clock_schedule_icon-icons.com_51085.ico",
                )
            if current_time>"9:59:50" and current_time<"10:00:00":
                count=0;
                while(count!=1):
                    time.sleep(5)
                    count+=1
                    notification.notify(
                    title = "TIME TABLE!",
                    message =  "BEE"+" SWAPNIL SIR",
                    app_icon = "calendar_clock_schedule_icon-icons.com_51085.ico",
                )
            if current_time>"9:59:50" and current_time<"10:00:00":
                count=0;
                while(count!=1):
                    time.sleep(5)
                    count+=1
                    notification.notify(
                    title = "TIME TABLE!",
                    message =  "BEE"+" SWAPNIL SIR",
                    app_icon = "calendar_clock_schedule_icon-icons.com_51085.ico",
                )
