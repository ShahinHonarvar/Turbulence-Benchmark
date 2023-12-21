
def find_divisors_in_range(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 2 to n-1 and check if each number divides n without leaving a remainder
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)

    # Return the list of all positive divisors of n that are between 2 and 9, both inclusive
    return divisors
