
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Loop through all divisors of n between 40 and 74 inclusive
    for i in range(40, 75):
        if n % i == 0:
            sum += i

    return sum
