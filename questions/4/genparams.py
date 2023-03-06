# This script generates three random unique non-negative parameter values for the question. params.txt comprises 100 values chosen by this script.

import random

params = []
counter = 0
while counter < 100:
    if counter < 10:
        first_idx, second_idx, third_idx = random.sample(range(0, 10), 3)
        counter += 1
    elif 10 <= counter < 50:
        first_idx, second_idx, third_idx = random.sample(range(10, 100), 3)
        counter += 1
    elif 50 <= counter < 70:
        first_idx, second_idx, third_idx = random.sample(range(100, 1000), 3)
        counter += 1
    else:
        first_idx, second_idx, third_idx = random.sample(range(0, 1000), 3)
        counter += 1

    three_random_values = (first_idx, second_idx, third_idx)
    if three_random_values not in params:
        params.append(three_random_values)

for p in params:
    print(f"{p[0]} {p[1]} {p[2]}")