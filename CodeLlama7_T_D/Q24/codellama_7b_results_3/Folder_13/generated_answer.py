
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Initialize the sum of divisors to 0
    sum_of_divisors = 0

    # Iterate from 472 to 827 (both inclusive)
    for i in range(472, 828):
        # Check if i is a divisor of n
        if n % i == 0:
            # If so, add it to the sum of divisors
            sum_of_divisors += i

    # Return the sum of all positive divisors of n that are between 472 and 827 (both inclusive)
    return sum_of_divisors
