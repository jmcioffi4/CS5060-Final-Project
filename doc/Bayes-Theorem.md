## Algorithm 2 - Bayes Theorem
*   The Problem:
    *   What is the probability of someone attending the gym `A` given the capacity at any hour on any day `B`?
    *   Assume the following:
        *   if the gym is more than 80% busy, then a gym goer will not go to the gym.
        *   if the gym is at 50%-80% capacity, then a gym goer will flip a coin to decide whether to go or not.
*   The Theorem
    *   `P(A|B) = P(B|A) * P(A) / P(B)`
    *   Where:
        *   `P(A|B)` is the conditional probability of `A` given `B`
            *   i.e. The probability of attending the gym given the capacity.
        *   `P(B|A)` is the conditional probability of `B` given `A`
            *   i.e. The probability of the capacity given attendance, depending on the coin flip.
        *   `P(A)` is the prior probability of `A`
            *   i.e. The prior probability of attending (will or will not).
        *   `P(B)` is the prior probability of `B`
            *   i.e. The prior probability of the gym's capacity
*   This data can be easily pulled from google map's data
    *   Collecting the data on local gyms in the area and using it in Bayes Theorem would satisfy the requirements of this algorithm and problem in this project.
    *   In the sake of time, we will generate mock data for the capacity of several gyms every hour of every day of the week and run Bayes Theorem on that data.