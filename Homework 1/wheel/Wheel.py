#Stephen Lambert
pocket= int(input("what is the pocket number:"))

if pocket ==0:
    print("The pocket is green")

if 1 <= pocket <= 10:
    if pocket % 2 == 0:
        print("The pocket is black")
    if pocket % 2 == 1:
        print("The pocket is red")

if 11 <= pocket <= 18:
    if pocket % 2 == 0:
        print("The pocket is red")
    if pocket % 2 == 1:
        print("The pocket is black")

if 19 <= pocket <= 28:
    if pocket % 2 == 0:
        print("The pocket is black")
    if pocket % 2 == 1:
        print("red")

if 29 <= pocket <= 36:
    if pocket % 2 == 0:
        print("red")
    if pocket % 2 == 1:
        print("The pocket black")

if pocket > 36:
    print(" there was an error, try again!")