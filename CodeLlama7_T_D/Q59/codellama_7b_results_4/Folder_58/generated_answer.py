
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the range of numbers from 1 to x-1
    for i in range(1, x):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-truncatable
            if is_left_truncatable(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check if a number is left-truncatable
def is_left_truncatable(n):
    while n > 0 and n % 10 != 0:
        n = int(str(n)[:-1]))
    return n == 0
