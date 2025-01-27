import schedule
import time
from main import main

def automate():
    """
    Automates the execution of the feedback analysis process.
    """
    schedule.every().day.at("10:00").do(main)
    print("Automation scheduled. Running daily at 10:00 AM.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    automate()
