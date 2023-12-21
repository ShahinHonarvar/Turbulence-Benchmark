
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n between 35 and 37, both inclusive
    for i in range(35, 38):
        if n % i == 0:
            sum += i

    # Return the sum of the divisors
    return sum
