
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate from 1 to x, checking for each number if it is a prime and if it is left-and-right-truncatable
    for i in range(1, x + 1):
        # If the current number is a prime number, check if it is left-and-right-truncatable by removing the leading leftmost and last rightmost digits
        if is_prime(i) and is_left_right_truncatable(i):
            primes.append(i) # Add the current number to the list of prime numbers

    # Sort the list of prime numbers in descending order
    primes.sort(reverse=True)

    return primes # Return the sorted list of prime numbers
