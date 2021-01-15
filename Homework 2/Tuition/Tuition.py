#Stephen Lambert
def main():

    tuition = int(input('Input the amount of tuition:'))
    increase = float(input('Enter the increase in tuition as a decimal:'))
    for years in range(1,6):
        tuition = tuition * (1+increase)
        print('$','\t', format(tuition,'.2f'))
        
main()



