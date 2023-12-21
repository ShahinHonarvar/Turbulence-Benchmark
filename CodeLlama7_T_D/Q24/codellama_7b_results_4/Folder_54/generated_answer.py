
def sum_of_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the sum of divisors to 0
    sum_divisors = 0

    # Iterate from 36 to 93 (both inclusive)
    for i in range(36, 94):

        # Check if i is a factor of n
        if n % i == 0:

            # Increment the sum of divisors by 1
            sum_divisors += 1

    # Return the sum of all positive divisors of n that are between 36 and 93, both inclusive
    return sum_divisors
