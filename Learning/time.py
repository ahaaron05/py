import time

print(f"The current time is: {time.ctime()}")
later = time.time() + 120
print(f"The time 2 minutes from now is: {time.ctime(later)}")