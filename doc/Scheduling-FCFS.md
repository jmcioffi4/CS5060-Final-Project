# Algorithm 3 - Scheduling FCFS
Main Problem
*   The main problem this implementation solves is the everyday issue of going to the gym... you know! Which machines are available? It's a first come first serve kind of world out there. This program generates a random number between 0 and 5,000 people as the number of people that visit the gym that day. Then it has a capacity of 100 machines at one hour. It determines who gets what machine based off of what is available, and counts how many people it had to turn away when there was not an available machine. 
*   *I tried to count the number of people who were thrown on a queue instead but couldn't get it to work for the life of me... sorry.*

Output
*   **File Output**: The output contains the gym's current known information at each individual hour of each day of the week. The outputs are detailing which person (identified by an ID number next to "person") is using what machine when. 
*   **Screen Output**: The output to the screen details the information about each day of the week, and how many people came to the gym on those days but couldn't get onto a machine. These are the people turned away. 
*   Interesting to see that this data shows sometimes first come first serve can work within restraints (in this case time on a 24hr clock vs capacity) but other times it fails and lets a lot of things get away.

*I would like to acknowledge I did consult with chatGPT to bounce ideas off of originally, and ended up learning quite a bit while putting this part (my part) together.*