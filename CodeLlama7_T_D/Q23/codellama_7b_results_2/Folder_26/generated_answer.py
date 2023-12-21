
def find_divisors_in_range(n):
    # Initialize the list of divisors
    divisors = []

    # Iterate from 83 to 95
    for i in range(83, 96):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
