# ALL DATA IS MADE UP IN THIS FILE
import sys
import numpy as np
import random

def bayes():
    WentOrNot = [[],[],[],[],[],[],[]]
    MOCK_DATA = { # how busy % wise the gym is for each hour in 24hrs
        'Sunday' : [np.random.randint(1, 101, size=24)],
        'Monday' : [np.random.randint(1, 101, size=24)],
        'Tuesday' : [np.random.randint(1, 101, size=24)],
        'Wednesday' : [np.random.randint(1, 101, size=24)],
        'Thursday' : [np.random.randint(1, 101, size=24)],
        'Friday' : [np.random.randint(1, 101, size=24)],
        'Saturday' : [np.random.randint(1, 101, size=24)]
    }

    # P(A|B) = P(B|A) * P(A) / P(B)
    # A = Attendance
    # B = the time of day and the week (how busy % wise AKA MOCK_DATA)
    index = 0
    for key, value in MOCK_DATA.items():
        for capacityPercentage in value:
            for hourPercentage in capacityPercentage:
                if hourPercentage > 80:
                    WentOrNot[index].append(False)
                elif hourPercentage > 50 or hourPercentage < 80:
                    WentOrNot[index].append(random.randint(0, 1) == 1)
                else: # hourPercentage < 50%
                    WentOrNot[index].append(True)
        index += 1

    index = 0

    for key, value in MOCK_DATA.items():
        print(key)
        print(value)
        for capacityPercentage in value:
            index2 = 0
            for hourPercentage in capacityPercentage:
                print(WentOrNot[index][index2])
                if WentOrNot[index][index2]:
                    hourPercentage += 1
                    value[index2] = hourPercentage
                index2 += 1
            index += 1
        print(key)
        print(value)
        sys.exit(0)