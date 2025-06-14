
def find_divisors_in_range(n):
    # Initialize a list of divisors
    divisors = []

    # Iterate from 3 to n
    for i in range(3, n + 1):

        # Check if i is a divisor of n
        if n % i == 0:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors in the specified range
    return divisors
