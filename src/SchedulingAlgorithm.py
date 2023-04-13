import random

def scheduling():
    # Define gym capacity
    gym_capacity = 100

    # Initialize list to track number of people who couldn't get in each day
    not_admitted = [0] * 7

    # Define a function to simulate gym usage for a given day
    def simulate_gym_usage(num_people):
        # Initialize queue for gym equipment usage requests
        queue = []
        # Loop through each person's equipment usage request
        for i in range(num_people):
            equipment = random.choice(["treadmill", "elliptical", "weights"])
            queue.append((f"Person {i+1}", equipment))
        # Loop through each item in the queue
        usage = {}
        for i in range(24):
            usage[i] = {}
        while queue:
            # Check if gym is at capacity
            if len(queue) > gym_capacity:
                not_admitted[random.randint(0, 6)] += len(queue) - gym_capacity
                queue = queue[:gym_capacity]
            # Remove the first item from the queue and grant the request
            person, equipment = queue.pop(0)
            hour = random.randint(0, 23)
            if equipment not in usage[hour]:
                usage[hour][equipment] = []
            if len(usage[hour][equipment]) < gym_capacity:
                usage[hour][equipment].append(person)

        # Output usage by hour to markdown file
        for hour in range(24):
            with open('gym_usage.md', 'a') as f:
                f.write(f"## Hour {hour}:00 - {hour+1}:00\n")
                f.write(f"Using machines:\n")
                for equipment in usage[hour]:
                    f.write(f"- {equipment.capitalize()}:\n")
                    for person in usage[hour][equipment]:
                        f.write(f"  - {person}\n")

    # Simulate gym usage for each day of the week
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in range(7):
        # Generate random number of people who want to go to the gym
        num_people = random.randint(0, 5000)
        with open('gym_usage.md', 'a') as f:
            f.write(f"# {days[day]}\n")
        simulate_gym_usage(num_people)

    # Print the number of people who couldn't get in each day
    print("Number of people who couldn't get into the gym each day:")
    for i, num in enumerate(not_admitted):
        print(f"Day {days[i]}: {num}")
