import sys
from BayesAlgorithm import bayes

try:
    while(True): # keep running till user exits
        print('---------------------------')
        userInput = input("**MENU**\n\n"
            "1 = Optimal Stopping\n\n"
            "2 = Bayes Theorem\n\n"
            "3 = Scheduling\n\n"
            "CTRL+C = Exit \n\n")

        if userInput.isdigit():
            userInput = int(userInput)
            if userInput == 1:
                print("Optimal Stopping")
            elif userInput == 2:
                bayes()
            elif userInput == 3:
                print("Scheduling")
            else:
                print("Invalid input.\nTry Again.")
        else:
            print("Invalid input.\nTry Again.")
        
except KeyboardInterrupt:
    print("Pressed ^C. Exiting.\n\n")
    sys.exit(0) 