# ALL DATA IS MADE UP IN THIS FILE
import numpy as np

def bayes():
    MAX_CAPACITY_OF_GYM = 100
    DAYS_OF_THE_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    DAYS_IN_A_MONTH = 31

    MOCK_DATA = {
        'Sunday' : [np.random.randint(1, 101, size=24)],
        'Monday' : [np.random.randint(1, 101, size=24)],
        'Tuesday' : [np.random.randint(1, 101, size=24)],
        'Wednesday' : [np.random.randint(1, 101, size=24)],
        'Thursday' : [np.random.randint(1, 101, size=24)],
        'Friday' : [np.random.randint(1, 101, size=24)],
        'Saturday' : [np.random.randint(1, 101, size=24)]
    }

    for key, value in MOCK_DATA.items():
        print(key)
        print(value)