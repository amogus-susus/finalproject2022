finalfinger = 0
quickcheck = " "
factcheck =" "
fingeramount = 0
handamount = 0
wowee = 0

def defaultCheck():
    quickcheck=input("Do you have the normal amount of hands?: ")
    for letter in quickcheck:
        letter = letter.lower()
    if(quickcheck == "yes" or quickcheck == "y"):
            print("Well, what makes you so special?")
            handamount = 2
            oddfinger()
    elif(quickcheck == "no" or quickcheck == "n"):
            irregularcount()
    else:
            quickcheck = int(input("Nope, Try Again: "))
            defaultCheck()
    
def irregularcount():
    factcheck = " "
    quickcheck = " "
    quickcheck = int(input("Well, how many hands do you have, then? "))
    if(quickcheck == 0):
        print("Well, I guess you don't have fingers, then.")

    elif(quickcheck == 2):
        print("That's the normal amount, you dingus.")
        handamount = 2
        oddfinger()
    elif(quickcheck == 1):
        print("Well, I guess that's normal, for some people.")
        handamount= 1
        oddfinger()
    elif(quickcheck>=3):
        handamount=quickcheck
        oddfinger()
        """
        factcheck = print("Uh, oh! You encountered an endless loop! How do you respond? ")
        for letter in factcheck:
            letter = letter.lower()
        if(quickcheck == "yes" or quickcheck == "y"):
            print("Huh... that's weird.")
            oddfinger()
        elif(quickcheck == "no" or quickcheck == "n"):
            print("Huh... would you... wanna trade?")
            oddfinger()
        else:  
            quickcheck =int(input("I couldn't be bothered to make more responses, Try Again: "))
            irregularcount()

            BONUS CONTENT: GET THIS PART TO WORK BY YOURSELF FOR MORE POINTS
            """
    else:
        quickcheck =int(input("Sorry, can't be bothered for more funny responses, Try Again: "))
        irregularcount()
    handamount = quickcheck
    


def oddfinger():
    quickcheck = " "
    quickcheck = input("Do you have the normal amount of fingers on each hand?: ")
    for letter in quickcheck:
        letter = letter.lower()
    if(quickcheck == "yes" or quickcheck == "y"):
        print("No need for further questions, then.")
        
    elif(quickcheck == "no" or quickcheck == "n"):
        goodness()
    else:
        quickcheck =int(input("Nope, Try Again: "))
        oddfinger()
    

def goodness():
    quickcheck = " "
    quickcheck = int(input("Well then, how many hands does this idea apply to?: "))
    if(quickcheck >0):
        wowee = quickcheck
        finalcheck()
    elif(quickcheck == 0):
        print("Then why did you say that?")
        finalcheck()
    else:
        quickcheck =int(input("No fooling around, Try Again: "))
        goodness()
        #zowee = weird hands
        #handamount = total hands

def finalcheck():
    quickcheck = " "
    zowee = handamount - wowee
    if(zowee < 0):
        print("That's a problem. You can't have more weird hands than the total")
        goodness()
    else:
        pass
    quickcheck = int(input("How many fingers do your weird hands have?: "))
    if(quickcheck == 5):
        print("Now, that's not very weird, is it?")
        fingeramount = handamount*5
    elif(1<=quickcheck<=4):
        print("Cool! That's [less] than the usual!")
        fingeramount = (zowee*quickcheck)+(handamount-wowee)
    elif(quickcheck > 5):
        print("Wow! That's [more] than the usual!")
        fingeramount = (zowee*quickcheck)+(handamount-wowee)


defaultCheck()
print("Uh oh! An error occurred! Now all of your fingers are mine! I mean gone!")
