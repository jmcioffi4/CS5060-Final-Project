import sys
from BayesAlgorithm import bayes
from SchedulingAlgorithm import scheduling
from OptimalStopping import optimal_stopping

try:
    while(True): # keep running till user exits
        print('---------------------------')
        userInput = input("**MENU**\n\n"
            "1 : Optimal Stopping\n"
            "2 : Bayes Theorem\n"
            "3 : Scheduling\n"
            "CTRL+C : Exit \n\n"
            ">> ")
        print('---------------------------')
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput == 1:
                optimal_stopping()
            elif userInput == 2:
                bayes()
            elif userInput == 3:
                scheduling()
            else:
                print("Invalid input.\nTry Again.")
        else:
            print("Invalid input.\nTry Again.")
        
except KeyboardInterrupt:
    print("Pressed ^C. Exiting.\n\n")
    sys.exit(0) 