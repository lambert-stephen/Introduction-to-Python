#Stephen Lambert
#Function to calcuate the average grade 
#main function
def main():
    #code that allows for use input
    test1 = int(input('Enter score 1: '))
    test2 = int(input('Enter score 2: '))
    test3 = int(input('Enter score 3: '))
    test4 = int(input('Enter score 4: '))
    test5 = int(input('Enter score 5: '))


    #calculates the total
    total = (test1 + test2 +test3 +test4 + test5)
    #Calculates the avaerage
    average = calc_average(test1,test2,test3,test4,test5)
    grade = total
    actual = determine_score(grade)
    #prints the letter grades
    print("Letter grade 1:", determine_score(test1))
    print("Letter grade 2:", determine_score(test2))
    print("Letter grade 3:", determine_score(test3))
    print("Letter grade 4:", determine_score(test4))
    print("Letter grade 5:", determine_score(test5))
    print("The average grade is:", average)

#function that calcuates the average and returns its value
def calc_average(test1,test2,test3,test4,test5):
        average =  (test1+test2+test3+test4+test5)/ 5
        return average
#Function that determines the grade based on the grade ranges
def determine_score(grade):
        if 90 <= grade <= 100:
            return 'A'
        elif 80 <= grade <= 89:
            return 'B'
        elif 70 <= grade <= 79:
            return 'C'
        elif 60 <= grade <= 69:
            return 'D'
        else:
            return 'F'
#end of main
main()









