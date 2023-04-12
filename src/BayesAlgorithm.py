# ALL DATA IS MADE UP IN THIS FILE
import numpy as np
import random

def run_bayes():
    WentOrNot = [[],[],[],[],[],[],[]]
    MOCK_DATA = { # how busy % wise the gym is for each hour in 24hrs
        'Sunday' : np.random.randint(1, 101, size=24),
        'Monday' : np.random.randint(1, 101, size=24),
        'Tuesday' : np.random.randint(1, 101, size=24),
        'Wednesday' : np.random.randint(1, 101, size=24),
        'Thursday' : np.random.randint(1, 101, size=24),
        'Friday' : np.random.randint(1, 101, size=24),
        'Saturday' : np.random.randint(1, 101, size=24)
    }

    # P(A|B) = P(B|A) * P(A) / P(B)
    # A = Attendance
    # B = the time of day and the week (how busy % wise AKA MOCK_DATA)
    index = 0
    for key, value in MOCK_DATA.items():
        for hourPercentage in value:
            if hourPercentage >= 80:
                WentOrNot[index].append(False)
            elif hourPercentage >= 50 and hourPercentage <= 80:
                WentOrNot[index].append(random.randint(0, 1) == 1)
            else: # hourPercentage < 50%
                WentOrNot[index].append(True)
        index += 1

    attend = 0
    hours = 0
    for day in WentOrNot:
        for hour in day:
            if hour:
                attend+=1
            hours+=1

    P_a = attend/hours

    attend = 0
    hours = 0
    for key, value in MOCK_DATA.items():
        for hour in value:
            if hour >= 80:
                attend+=1
            hours+=1
    
    P_b = attend/hours

    attend = 0
    hours = 0
    for key, value in MOCK_DATA.items():
        for hour in value:
            if hour >= 50:
                attend+=1
            hours+=1

    P_b_a = attend/hours
    P_a_b = P_b_a * P_a / P_b

    return P_a, P_b, P_b_a, P_a_b

def bayes():
    for i in range (1,6):
        print(f"Gym {i}:")
        P_a, P_b, P_b_a, P_a_b = run_bayes()
        print(f"\tP(A) = {P_a}")
        print(f"\tP(B) = {P_b}")
        print(f"\tP(B|A) = {P_b_a}")
        print(f"\tP(A|B) = {P_a_b}")
