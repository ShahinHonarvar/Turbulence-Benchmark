
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all positive integers between 120 and 349, both inclusive
    for i in range(120, 350):
        # Check if the current integer is a divisor of n
        if n % i == 0:
            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of all positive divisors of n that are between 120 and 349, both inclusive
    return divisors
