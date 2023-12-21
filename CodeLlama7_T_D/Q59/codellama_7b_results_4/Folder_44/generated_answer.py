
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Iterate through the tuple
    for i in range(len(tuple)):

        # Get the current number in the tuple
        num = tuple[i]

        # Check if the number is a prime number
        if is_prime(num):

            # Add the prime number to the list
            prime_list.append(num)

    # Sort the list of prime numbers in ascending order
    prime_list.sort()

    # Return the sorted list of prime numbers
    return prime_list

# Check if a number is a prime number
def is_prime(n):

    # Check if the number is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):

            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:

                # Return False if the number is divisible by any number between 2 and the square root of the number
                return False

    # If the number is greater than 1, return True
    return True
