
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all numbers between 13 and 62, inclusive
    for i in range(13, 63):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors found in the specified range
    return divisors
