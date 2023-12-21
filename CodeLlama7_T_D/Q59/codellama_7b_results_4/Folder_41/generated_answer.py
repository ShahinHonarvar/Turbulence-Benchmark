
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate from 2 to x - 1
    for i in range(2, x - 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if all left-truncatable prime numbers less than i are prime
            if all_left_truncatable_prime(i - 1) == []:

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
