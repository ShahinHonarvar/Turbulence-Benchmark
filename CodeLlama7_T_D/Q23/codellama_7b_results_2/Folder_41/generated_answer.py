
def find_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 2 to n-1
    for i in range(2, n):

        # Check if i is a divisor of n
        if n % i == 0:

            # If it is a divisor, add it to the list
            divisors.append(i)

    # Return the list of divisors
    return divisors
