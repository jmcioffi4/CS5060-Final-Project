# CS5060 Final Project (Implementation)

## Algorithm 1 - Optimal Stopping
*   The Problem:
    *   Gyms usually offer discounts or deals on new memerships in order to incentivize people to join after making their New Year's resolutions, but when is the best time to end those deals, since people tend to stop going to the gym and either don't take advantage of or cancel their memberships? At what point will the gym start losing money on their members instead of making money from them by offering these deals? The graph produced from this year-long distribution shows, at its peak, the best day for a gym to end its deal on memberships after the New Year in order to make the most possible money.
    *   When should the gym end deals on memberships given
        * (A) When people stop going to the gym after starting their New Year's Resolutions?
*   This data is synthesized from survey information found online about how long people follow through on their New Year's Resolutions

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

## Algorithm 3 - Scheduling
*  The problem:
    *   Personal Training: Use a scheduling algorithm to optimize personal training schedules for both trainers and clients. The algorithm can take into account the availability of the trainer and the preferences of the client, as well as their fitness goals and current fitness level.