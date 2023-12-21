
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the divisors of n in the specified range
    for i in range(32, 91):
        if n % i == 0:
            sum += i

    # Return the sum of all positive divisors of n that are between 32 and 90, both inclusive
    return sum
