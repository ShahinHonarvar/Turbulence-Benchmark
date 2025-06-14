
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum of divisors to 0
    sum_of_divisors = 0

    # Iterate over the range of numbers from 39 to 57 (inclusive)
    for i in range(39, 58):
        # Check if i is a factor of n
        if n % i == 0:
            # Add the factor to the sum of divisors
            sum_of_divisors += i

    # Return the sum of divisors within the specified range
    return sum_of_divisors
