import math
def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n%i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return [d for d in divisors if d in range(1, 8)]
