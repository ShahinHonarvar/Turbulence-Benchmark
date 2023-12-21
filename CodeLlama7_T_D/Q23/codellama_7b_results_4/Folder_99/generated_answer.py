
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 378 to 782, both inclusive
    for i in range(378, 783):
        # Check if 'i' is a divisor of 'n'
        if n % i == 0:
            # If it is a divisor, add it to the list
            divisors.append(i)

    # Return the list of all positive divisors of 'n' that are between 378 and 782, both inclusive
    return divisors
