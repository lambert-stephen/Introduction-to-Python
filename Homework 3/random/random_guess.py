#Stephen Lambert
#This programsf generates a random number guessing game
#The prgram gives the user hints and displays the correct random number
#generates a random number
import random
#main function for the game
def main():
    answer = 0
    number = random.randint(1,100)
    while answer < 10:
         guess = int(input('Guess the random number:'))
         answer = answer +1
         if guess < number:
            print('Your guess is to low')

         if guess > number:
            print('Your guess is to high')

         if guess == number:
            print('Congratulations. You guessed the correct number.')


    gen_number(number)
    print('The correct number was', number)

def gen_number(number):
    return number


main()