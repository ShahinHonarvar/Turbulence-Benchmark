# This script generates random pairs of suitable parameter values for the question. params.txt comprises 20 values chosen manually, and a further 80 values chosen by this script.

import random

params = []
while len(params) < 80:
    first = random.randint(0, 1000)
    second = random.randint(first, 1001)
    pair = (first, second)
    if pair not in params:
        params.append(pair)

for p in params:
    print(f"{p[0]} {p[1]}")
