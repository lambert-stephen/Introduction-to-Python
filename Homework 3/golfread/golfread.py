#This program reads the line in the file, and displays them.
#Stephen Lambert
def main():
    try:
        #opens file for reading
        infile = open('golf.txt', 'r')
        name = infile.readline()
        while name != '':
            score = infile.readline()
            
            name = name.rstrip('\n')
            score = score.rstrip('\n')
            print(name + " scored a " + score)
            name = infile.readline()
        infile.close()
    except ValueError:
        print("Error: File contains bad data")

    except IOrror:
        print("ERROR: File cannot be found")
main()