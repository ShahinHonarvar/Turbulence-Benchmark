
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Iterate over the tuple of positive integers
    for num in tuple:

        # Check if the number is prime
        if is_prime(num):

            # Add the prime number to the list
            prime_list.append(num)

# Return the sorted list of all left-truncatable prime numbers less than x
return sorted(prime_list, reverse=True)

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True
