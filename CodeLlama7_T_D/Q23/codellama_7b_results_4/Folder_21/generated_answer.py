
def find_divisors_in_range(n):
    # Check if n is a positive integer
    if not (type(n) == int and n > 0):
        raise ValueError("Input must be a positive integer")

    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all numbers between 120 and 349
    for i in range(120, 350):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
