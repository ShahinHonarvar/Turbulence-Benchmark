
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 59 to 88 (both inclusive)
    for i in range(59, 89):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors (if any)
    return divisors
