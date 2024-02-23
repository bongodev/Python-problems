# 33. **Countdown Timer**: Create a countdown timer from 10 to 0 using a `while` loop.
# import time
from time import sleep

start = int(input("Where to start from: "))

while start >= 0:
    print(start)
    start = start - 1
    # add delay
    # time.sleep(1)
    sleep(5 * 3600)
