
def find_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 4 to 5 inclusive
    for i in range(4, 6):

        # Check if i is a divisor of n
        if n % i == 0:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
