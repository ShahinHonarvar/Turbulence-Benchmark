# This script generates four random suitable parameter values for the question. params.txt comprises 20 values
# chosen manually, and a further 80 values chosen by this script.

import random

params = []
while len(params) < 80:
    # Exclusive of 0 since 0 is not a divisor of any integer. Both values are unique.
    first_divisor, second_divisor = random.sample(range(1, 100), 2)  
    first_idx = random.randint(0, 1000)
    second_idx = random.randint(first_idx, 1001)
    four_random_values = (first_divisor, second_divisor, first_idx, second_idx)
    if four_random_values not in params:
        params.append(four_random_values)

for p in params:
    print(f"{p[0]} {p[1]} {p[2]} {p[3]}")