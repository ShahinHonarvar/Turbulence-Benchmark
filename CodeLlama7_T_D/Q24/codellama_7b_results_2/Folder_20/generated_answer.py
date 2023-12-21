
def sum_of_divisors_in_range(n):
    # Check that n is positive
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Initialize the sum to 0
    sum = 0
    # Iterate over all divisors of n between 28 and 81, both inclusive
    for i in range(28, 82):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
