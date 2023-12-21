
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 39 to 43 (both inclusive)
    for i in range(39, 44):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If it is a divisor, add it to the list
            divisors.append(i)

    # Return the list of divisors (if any)
    return divisors
