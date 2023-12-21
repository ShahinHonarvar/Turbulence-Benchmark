import math
def sum_of_divisors_in_range(n):
    if n <= 12:
        return 0
    elif n <= 36:
        return (1 + 2 * n) * (1 + n)
    elif n <= 48:
        return (1 + 2 * n) * (1 + n + math.factorial(int(math.sqrt(n))))
