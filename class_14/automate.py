import schedule
import time
from datetime import datetime

def write_field():
    with open("schedule_demo.txt", "w") as f:
        f.write(f"Hellow! the time is {datetime.now()}")

schedule.every(1).minutes.do(write_field)


while True:
    schedule.run_pending()
    time.sleep()


#this code will make a file schedule_demo.txt which will always run


