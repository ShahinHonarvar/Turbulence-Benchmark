
def find_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The argument must be a positive integer")

    # Initialize the list of divisors
    divisors = []

    # Iterate from 469 to 682 (both inclusive)
    for i in range(469, 683):
        # Check if i is a divisor of n
        if n % i == 0:
            # Add i to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
