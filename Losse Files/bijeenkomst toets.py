import time
launch = int(input("enter a number\n "))

while launch > 0:
    print(launch)
    time.sleep(1)
    launch = launch -1
if launch == 0:
    print("launched!!")