import math
def find_divisors_in_range(n):
    if n < 111 or n > 508:
        return []
    if n <= 4:
        return [i for i in range(1, int(math.ceil(math.sqrt(n)) + 1) if n % i == 0)]
    else:
        return [i for i in range(1, int(n ** .5) + 1) if n % i == 0]
