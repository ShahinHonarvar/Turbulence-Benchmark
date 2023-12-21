
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum of divisors to 0
    sum_of_divisors = 0

    # Iterate from 13 to 62 (inclusive)
    for i in range(13, 63):
        # Check if i is a divisor of n
        if n % i == 0:
            # Add i to the sum of divisors
            sum_of_divisors += i

    # Return the sum of divisors between 13 and 62 (inclusive) or 0 if no such divisors exist
    return sum_of_divisors
