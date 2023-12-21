
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate from 1 to x-1
    for i in range(1, x):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-truncatable prime
            if is_left_truncatable_prime(i):

                # Add i to the result list
                result.append(i)

    # Sort the result list in descending order
    result.sort(reverse=True)

    # Return the result list
    return result

# Check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is greater than 1
    return True

# Check if a number is left-truncatable prime
def is_left_truncatable_prime(n):

    # Check if n contains any 0
    if '0' in str(n):

        # Return False if n contains any 0
        return False

    # Iterate from the leading leftmost digit of n to 1
    for i in range(len(str(n)))-1, -1, -1:

        # Check if the number obtained by removing the leading leftmost digit of n is prime
        if is_prime(int(str(n)[i:])))

            # Return False if the number obtained by removing the leading leftmost digit of n is not prime
            return False

    # Return True if all numbers obtained by removing the leading leftmost digit of n are prime
    return True
