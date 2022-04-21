# Write your code here :-)
import cmpt120image
import cmpt120colours

#Main Program Loop
print("\n1: Load Colour File\n2: Print All Colours\n3: Select Colour\n4: Find Closest Colour\n5: Display (Save) Colour Scheme\n0: Quit")
def menu():
    while True:
        userInput = input("\nSelect an option: ")
        #Load Colour File
        if (userInput == "1"):
            cmpt120colours.loadColourFile()
        #Print all colours
        elif(userInput == "2"):
            cmpt120colours.printColours()
        #Select Colour
        elif(userInput == "3"):
            cmpt120colours.selectColour()
        #Find Closest Colour
        elif(userInput == "4"):
            cmpt120colours.findClosest()
        #Display color scheme
        elif(userInput == "5"):
            cmpt120colours.colourScheme()
        elif(userInput == "0"):
            break
        else:
            print("Please enter a number between 0 and 5")
menu()
