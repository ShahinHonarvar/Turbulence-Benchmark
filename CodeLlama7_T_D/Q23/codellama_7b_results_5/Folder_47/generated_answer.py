
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 1 to n, checking if each number is a divisor of n
    for i in range(1, n + 1):
        # If i is a factor of n, add it to the list of divisors
        if n % i == 0:
            divisors.append(i)

    # Return the list of divisors found in the specified range, or an empty list if no such divisors exist
    return divisors
