
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 111 to 508
    for i in range(111, 509):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If it is a divisor, add it to the list
            divisors.append(i)

    # Return the list of divisors
    return divisors
