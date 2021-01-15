#Stephen Lambert
#Program that calculates the property tax and prints the value
#main function
def main():
    #allows for user input
    property_value = int(input("Enter the property's actual value: "))
    #function call used for calculations
    calc_assessment_tax(property_value)
#function to calculate property tax
def calc_assessment_tax(property_value):
    assessment_value = property_value * 0.6
    print('The assessment value is:', format(assessment_value, '.2f'))
    calc_assessment_tax = assessment_value * 0.0072
    print('The property tax is:', format(calc_assessment_tax, '.2f'))
    #end of main
main()