
import cmpt120image

colourDict = {}
#PART 1 - User Interface, Load and Print Dictionary
def rgbToHex(rgbList):
    hexValR = hex(int(rgbList[1]))[2:]
    hexValG = hex(int(rgbList[2]))[2:]
    hexValB = hex(int(rgbList[3]))[2:]

    if (len(hexValR) == 1):
        hexValR = "0" + hexValR
    if (len(hexValG) == 1):
        hexValG = "0" + hexValG
    if (len(hexValB) == 1):
        hexValB = "0" + hexValB

    return("#" + ((str(hexValR) + str(hexValG) + str(hexValB))).upper())
def loadColourFile():
    file = open("colours.csv")
    colourCount = 0
    for line in file:
        lineList = line.split(",")

        dictKey = (int(lineList[1]), int(lineList[2]), int(lineList[3]))

        dictValHex = rgbToHex(lineList)
        dictValColor = [lineList[0].capitalize(), dictValHex]

        if dictKey not in colourDict:
            colourDict.update({dictKey : dictValColor})
            colourCount += 1

    print("\nThe file has been processed and " + str(colourCount) + " colours were entered into the dictionary")

def printHeader(first, second, third, fourth, fifth):
  print("\n{: <10}".format(first) , "{: >5}".format(second), "{: >5}".format(third), "{: >5}".format(fourth), "{: >5}".format(fifth))
  print("\n{: <1}".format(len(first) * '-'), "{: >5}".format(len(second) * '-'), "{: >5}".format(len(third) * '-'), "{: >5}".format(len(fourth) * '-'), "{: <5}".format(len(fifth) * '-'))

def printColours():
    printHeader("Colour Name", "Red", "Green", "Blue", "Hex")

    for keys, values in colourDict.items():
        print("{: <10}".format(values[0]), "{: >5}".format(keys[0]) , "{: >5}".format(keys[1]) , "{: >5}".format(keys[2]) , "{: >5}".format(values[1]))

#PART 2 - Select Colour
def selectColour():
    print("Enter the RGB values of your colour")
    userColourR = int(input("R: "))
    userColourG = int(input("G: "))
    userColourB = int(input("B: "))

    userRGB = (userColourR, userColourG, userColourB)
    print(userRGB)
    sampleFound = False
    for rgbItem in colourDict:
       if rgbItem == userRGB:
           sampleFound = True
           print("Colour " + str(userRGB) + " is " +  colourDict[rgbItem][0] + " and has hex code " + colourDict[rgbItem][1])

    if (sampleFound == False):
        print("\nColour " + str(userRGB) + " was not found. Would you like to:\n1. Enter a name for this color\n2. Return to the main menu")
        userInput = input("Select an option: ")
        if (userInput == "1"):

            userColourName = input("What is the colour's name? ")
            newColor = [userColourName, str(userRGB[0]), str(userRGB[1]), str(userRGB[2])]
            userHexCode = addToDict(newColor, userColourName, userRGB)
            print("Colour " + str(userRGB) + " is " + userColourName + " and has hex code " + userHexCode + ".")

def addToDict(newColor, name, rgb):

        dictValHex = rgbToHex(newColor)
        dictValColor = [name.capitalize(), dictValHex]

        if rgb not in colourDict:
            colourDict.update({rgb : dictValColor})
        return dictValHex

#PART 3 - Finding the Closest Colour
def findClosest():
    print("Enter the RGB values of your colour")
    userColourR = int(input("R: "))
    userColourG = int(input("G: "))
    userColourB = int(input("B: "))

    userRGB = (userColourR, userColourG, userColourB)
    print(userRGB)
    sampleFound = False
    for rgbItem in colourDict:
       if rgbItem == userRGB:
           sampleFound = True
           print("Colour " + str(userRGB) + " is " +  colourDict[rgbItem][0] + " and has hex code " + colourDict[rgbItem][1])

    if (sampleFound == False):

        sumMin = (255 * 3)
        currentClosest = ()
        for rgbItem in colourDict:
            rVal = abs(userRGB[0] - rgbItem[0])
            gVal = abs(userRGB[1] - rgbItem[1])
            bVal = abs(userRGB[2] - rgbItem[2])
            absSum = rVal + gVal + bVal
            if (absSum < sumMin):
                sumMin = absSum
                currentClosest = rgbItem

        print("The closest color to " + str(userRGB) + " is " + str(currentClosest) + ", " + colourDict[currentClosest][0] + " with hex code " + colourDict[currentClosest][1])
        print("The absolute difference between the two colours is " + str(sumMin) +".")


#PART 4 - Display Colour Scheme
def colourScheme():
    print("Enter the RGB values of your colour")
    userColourR = int(input("R: "))
    userColourG = int(input("G: "))
    userColourB = int(input("B: "))

    userRGB = (userColourR, userColourG, userColourB)

    print("Which colour scheme do you wish to display?\nM: Monochrome\nC: Complementary")

    userSchemeInput = input("\nSelect an option: ")

    if (userSchemeInput == "M" or userSchemeInput == "m"):
        img = cmpt120image.getBlackImage(240, 240)

        h = len(img)
        w = len(img[0])

        #Full square
        for row in range(h):
            for col in range(w):
                img[row][col] = [userColourR, userColourG, userColourB]

        #Top Left
        for row in range(h // 3):
            for col in range(w // 3):
                img[row][col] = [userColourR + int((255 - userColourR) * 0.8), userColourG + int((255 - userColourG) * 0.8),
                userColourB + int((255 - userColourB) * 0.8)]
        #Top Right
        for row in range(h // 3):
            for col in range(w - (w // 3), w):
                img[row][col] = [userColourR + int((255 - userColourR) * 0.5), userColourG + int((255 - userColourG) * 0.5),
                userColourB + int((255 - userColourB) * 0.5)]
        #Bottom Left
        for row in range((h - (h //3)), h):
            for col in range(w // 3):
                img[row][col] = [int((userColourR) * 0.5), int((userColourG) * 0.5),
                int((userColourB) * 0.5)]
        #Bottom Right
        for row in range((h - (h //3)), h):
            for col in range(w - (w // 3), w):
                img[row][col] = [int((userColourR) * 0.8), int((userColourG) * 0.8),
                int((userColourB) * 0.8)]


    elif (userSchemeInput == "C" or userSchemeInput == "c"):
        img = cmpt120image.getBlackImage(480, 240)

        h = len(img)
        w = len(img[0]) // 2

        #Full square
        for row in range(h):
            for col in range(w):
                img[row][col] = [userColourR, userColourG, userColourB]

        #Top Left
        for row in range(h // 3):
            for col in range(w // 3):
                newColor = lighten([userColourR, userColourG, userColourB], 0.8)
                img[row][col] = newColor
        #Top Right
        for row in range(h // 3):
            for col in range(w - (w // 3), w):
                newColor = lighten([userColourR, userColourG, userColourB], 0.5)
                img[row][col] = newColor
        #Bottom Left
        for row in range((h - (h //3)), h):
            for col in range(w // 3):
                newColor = darken([userColourR, userColourG, userColourB], 0.5)
                img[row][col] = newColor
        #Bottom Right
        for row in range((h - (h //3)), h):
            for col in range(w - (w // 3), w):
                newColor = darken([userColourR, userColourG, userColourB], 0.8)
                img[row][col] = newColor

        h = h
        w = w * 2
        half = w // 2

        compR = (255 - userColourR)
        compG = (255 - userColourG)
        compB = (255 - userColourB)

        #Full square
        for row in range(h):
            for col in range((w - (half)), w):
                img[row][col] = [compR, compG, compB]

        #Top Left
        for row in range(h // 3):
            for col in range(half, half  + (half // 3)):
                newColor = lighten([compR, compG, compB], 0.8)
                img[row][col] = newColor
        #Top Right
        for row in range(h // 3):
            for col in range((half + (w // 3)), w):
                newColor = lighten([compR, compG, compB], 0.5)
                img[row][col] = newColor
        #Bottom Left
        for row in range((h - (h //3)), h):
            for col in range(half, half  + (half // 3)):
                newColor = darken([compR, compG, compB], 0.5)
                img[row][col] = newColor
        #Bottom Right
        for row in range((h - (h //3)), h):
            for col in range((half + (w // 3)), w):
                newColor = darken([compR, compG, compB], 0.8)
                img[row][col] = newColor


    cmpt120image.showImage(img)
    cmpt120image.saveImage(img, "csheme.png")

def darken(colour, percentage):
    r = colour[0]
    g = colour[1]
    b = colour[2]
    return ((int(r * percentage), int(g * percentage), int(b * percentage)))

def lighten(colour, percentage):
    r = colour[0]
    g = colour[1]
    b = colour[2]
    return ((colour[0] + int((255 - r) * percentage), colour[1] + int((255 - g) * percentage), colour[2] + int((255 - b) * percentage)))

