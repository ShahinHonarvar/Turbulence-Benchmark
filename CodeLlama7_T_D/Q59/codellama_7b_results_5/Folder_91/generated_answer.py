
def all_left_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[0]
    list = []
    # Check if x is prime
    if is_prime(x):
        # Add x to the list
        list.append(x)

    # Loop through all numbers less than x
    for i in range(2, x):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i contains no 0
            if '0' not in str(i):
                # Add i to the list
                list.append(i)

    # Sort the list in descending order
    list.sort(reverse=True)

    # Return the list
    return list

def is_prime(n):

    # Check if n is less than 2
    if n < 2:
        return False

    # Loop through all numbers up to and including the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n
        if n % i == 0:
            return False

    # If we reach this point, then n is prime
    return True
