"""
Generate a realistic synthetic Boston College Catering dataset.

This script creates random employee shifts, locations, hours, and tips,
then exports the dataset to a CSV file for analysis.
"""
import pandas as pd
import random

days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
times = ["Morning", "Afternoon", "Evening"]
workers = ["Alice", "Bob", "Charlie", "David", "Eve"]
locations = ["Messina", "Gasson Hall", "O'Neill Library", "St. Mary's Hall", "President's Suite", "2101", "Murray", "SAAS", "Mcelroy", "Stokes"]

experience = dict()
for i in workers:
    experience[i] = random.randint(1, 10)  # Random experience level between 1 and 10 years


rows = list()

for i in range (200):  # Generate 200 random entries
    day = random.choice(days)
    time = random.choice(times)
    worker = random.choice(workers)
    location = random.choice(locations)
    hours = random.randint(2, 12)
    tips = 0.0

    # Determine tip cap based on location , day, and experience
    if location in ["O'Neill Library","SAAS", "Mcelroy"]:
        cap = 12
    elif location in ["Gasson Hall", "St. Mary's Hall", "Stokes"]:
        cap = 20
    elif location in ["Messina", "2101", "Murray", "President's Suite"]:
        cap = 28

    if time == "Evening":
        cap = cap * 1.25

    if day in ["Saturday", "Sunday","Friday"]:
        cap = cap * 1.45

    cap = cap * (1 + (random.randint(0, experience[worker]) / 10))  # Increase cap based on experience
    
    for i in range(hours):
        tips =  round(random.uniform(0, cap) + tips)
    
    rows.append({"Day": day, "Time": time, "Worker": worker, "Location": location, "Hours": hours, "Tips": round(tips, 2)})
   
df = pd.DataFrame(rows)

print (df.head(10))

csv_file = "random_catering_data.csv"
df.to_csv(csv_file)