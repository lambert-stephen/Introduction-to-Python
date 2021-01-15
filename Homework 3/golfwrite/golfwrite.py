#This program allows you to write the name and score of a player to the file golf.txt.
#Stephen Lambert
outfile = open('golf.txt', 'w')
while True:
    name = input("Player's name(click enter to quit):")
    if name == "":
        break
    score = input("Enter the player's score:")
    outfile.write(name + "\n")
    outfile.write(str(score) + "\n")
outfile.close()