import sys
import matplotlib.pyplot as plt
import numpy.random as rnd

def optimal_stopping():
    num_of_days = 365
    solution_found_count = {}
    optimal_solution_found_count = {}
    for i in range(1, num_of_days):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i)] = 0
    
    for experiment in range(100):
        # implement beta distribution because a lot of people start going to the gym in January, and then it drops off
        # used 2 and 25 arbitrarily to mimic a right skewed distribution based on desmos
        active_members = rnd.beta(2, 25, num_of_days)
        max_members = max(active_members) #finds the time when the most people are going to the gym and using their membership

        for i in range(1, num_of_days):
            for amount_of_members in active_members[i:-1]: #for each amount of members, starting at the second day of the year
                if amount_of_members > max(active_members[0:i]): #if the amount of members surpasses the active members at any point,
                    solution_found_count[str(i)] += 1 
                    if amount_of_members == max_members: 
                        optimal_solution_found_count[str(i)] += 1
                    
                    break

    print(active_members)
    print(max_members)

    x, y = zip(*optimal_solution_found_count.items())

    print(optimal_solution_found_count)
    plt.xlabel('Day', fontsize=18)
    plt.ylabel('Optimal Solution Found Count', fontsize=18)
    plt.plot(x,y)
    plt.show()