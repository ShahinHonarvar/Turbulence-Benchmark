# This script generates random suitable parameter value for the question. params.txt comprises 100 values chosen by this script.

import random

params = []
while len(params) < 100:
    num = random.randint(1, 1000)
    if num not in params:
        params.append(num)

for p in params:
    print(f"{p[0]}")
