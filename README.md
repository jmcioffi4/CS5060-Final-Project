# CS5060 Final Project (Implementation)

## Algorithm 1 - Optimal Stopping
*   The Problem:
    *   When should the gym end deals on memberships given
        * (A) When people stop going to the gym after starting their New Year's Resolutions?
*   This data is found from survey information found online about how long people follow through on their New Year's Resolutions

## Algorithm 2 - Bayes Theorem
*   The Theorem
    *   `P(A|B) = P(B|A) * P(A) / P(B)`
    *   Where:
        *   `P(A|B)` is the conditional probability of `A` given `B`
        *   `P(B|A)` is the conditional probability of `B` given `A`
        *   `P(A)` is the prior probability of `A`
        *   `P(B)` is the prior probability of `B`
*   The problem the algorithm will solve:
    *   What is the probability of attending the gym (A) given
        *   The capacity at any hour on any day (B)
    *   Assume the following:
        *   if the gym is more than 80% busy, then a gym goer will not go to the gym.
        *   if the gym is at 50%-80% capacity, then a gym goer will flip a coin to decide whether to go or not.
*   This data can be easily pulled from google map's data
    *   Collecting the data on local gyms in the area and using it in Bayes Theorem would satisfy the requirements of this algorithm and problem in this project.

## Algorithm 3 - Scheduling
*  The problem:
    *   Personal Training: Use a scheduling algorithm to optimize personal training schedules for both trainers and clients. The algorithm can take into account the availability of the trainer and the preferences of the client, as well as their fitness goals and current fitness level.