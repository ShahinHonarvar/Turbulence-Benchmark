
def find_divisors_in_range(n):
    # Initialize a list to store the divisors
    divisors = []

    # Iterate from 1 to n-1
    for i in range(1, n):

        # Check if i is a divisor of n
        if n % i == 0:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors in the specified range
    return divisors
