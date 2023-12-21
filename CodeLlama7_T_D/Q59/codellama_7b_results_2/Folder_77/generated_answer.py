
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through the tuple of integers
    for i in range(len(tuple)):

        # Check if the current integer is a prime number
        if is_prime(tuple[i]):

            # If the current integer is a prime number, append it to the list of prime numbers
            prime_list.append(tuple[i])

    # Return the sorted list of prime numbers
    return sorted(prime_list, reverse=True)

# Define a function to check if an integer is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through the range of 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if n is divisible by i
            if n % i == 0:

                # If n is divisible by i, return False
                return False

    # If n is greater than 1 and is not divisible by any number in the range of 2 to the square root of n, return True
    return True
