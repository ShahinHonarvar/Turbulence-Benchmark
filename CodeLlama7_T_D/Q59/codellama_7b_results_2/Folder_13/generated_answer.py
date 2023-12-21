
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Iterate through the tuple
    for i in range(len(tuple)):
        # Get the current number
        current_number = tuple[i]

        # Check if the current number is a prime number
        if is_prime(current_number):
            # Add the current number to the list of prime numbers
            prime_list.append(current_number)

    # Sort the list of prime numbers in ascending order
    prime_list = sorted(prime_list)

    return prime_list


def is_prime(n):

    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, then it is prime
    return True
