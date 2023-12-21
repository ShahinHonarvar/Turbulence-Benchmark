
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of positive integers
    for x in tuple:

        # If the number is a prime number, add it to the list
        if is_prime(x):
            prime_numbers.append(x)

        # If the number is not a prime number, remove the last rightmost digit and check if it is a prime number
        else:
            while not is_prime(x):
                x = int(str(x)[0:-1]))

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
