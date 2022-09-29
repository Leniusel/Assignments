#Doris Tran
#Question 15.1 from M06 Programming Assignment
#This program will make three different processes. Each will wait a random number of seconds between 0-1, print the current time, exit
import time
import datetime
import multiprocessing
import random
import os


#15.1
#function to calculate the wait time before the program prints the current time
def whattime(isit):
    wait = random.uniform(0, 1)
    process = os.getpid()
    print("Process %s Wait Time is %s seconds: %s" % (process, wait, isit))  
    time.sleep(wait)

#multiprocess
if __name__ == "__main__":
    #For three different process
    for n in range(3):
        #find the epoch and convert it to string
        now = time.time()
        date = time.ctime(now)
        #state what being processed
        p = multiprocessing.Process(target=whattime,
          args=("Current time is %s" % date,))
        #start
        p.start()
#exit when done