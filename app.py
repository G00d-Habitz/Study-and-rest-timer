import pygame, timeit

goaltime = int(input("How many seconds would you like to count down from? "))
starttime = timeit.default_timer()

while timeit.default_timer() - starttime < goaltime:
    timedown = goaltime - (timeit.default_timer() - starttime)
    print(f"Current time is: {int((timedown)/60)}:{(int(timedown) % 60)}")

print("Bzzzt! The time is up!")
