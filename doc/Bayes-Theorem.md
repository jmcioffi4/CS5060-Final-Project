## Algorithm 2 - Bayes Theorem
*   The Problem
    *   We are estimating the probability of gym goers showing up at different times of the week based on the percentage of how busy the gym is at each hour of the day... Sounds a bit stupid but hear me out.
    *   We want to base this off of an individual viewpoint. We are running the program from the gym goers mindset. If the gym is more than 80% busy, then we ain't goin to the gym.
        *   If the gym is between 50%-80% busy, its a toss up. Do we really want to deal with this right now? Maybe the gym goer will just go later. Maybe they'll be productive and go now.
        *   If the gym is less than half busy, then there's clearly enough space the gym goer will go to the gym.
*  The Theorem
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
*   The Data
    *   The data in this algorithm is randomly generated.