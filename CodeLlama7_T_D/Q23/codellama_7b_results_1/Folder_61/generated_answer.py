
def find_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Initialize the list of divisors
    divisors = []

    # Iterate from 2 to n-1 and check for divisibility
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)

    return divisors
