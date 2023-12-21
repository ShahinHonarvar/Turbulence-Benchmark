
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum to 0
    sum = 0

    # Iterate from 40 to 74 (both inclusive)
    for i in range(40, 75):

        # Check if i is a divisor of n
        if n % i == 0:

            # Add i to the sum
            sum += i

    # Return the sum
    return sum
