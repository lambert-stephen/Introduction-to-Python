#Stephen Lambert
#Python program to find the day approximation population
#variables defined below
starting = int(input("Starting number of organisms: "))
increase = float(input("Enter the average daily increase: "))/100.0
#code that allows for user input
days = int(input("Number of days to multiply: "))
day_1 = True
#print statement
print("Day Approximate\tPopulation")
#for loop
for days in range(starting, days+ 1):
    if day_1:
        print(1, '\t', starting)
        day_1 = False
    add = starting * increase
    starting= starting + add
    #prints the output
    print(days, '\t', starting)
