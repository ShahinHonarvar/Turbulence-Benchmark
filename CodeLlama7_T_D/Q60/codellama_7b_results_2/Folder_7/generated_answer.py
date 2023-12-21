
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all the prime numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-and-right-truncatable
            if is_left_right_truncatable(i):
                # If i is both a prime number and left-and-right-truncatable, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers that are both prime and left-and-right-truncatable
    return sorted(prime_numbers)

# Check if a number is prime by iterating from 2 to the square root of the number
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

# Check if a number is left-and-right-truncatable by repeatedly removing the leading leftmost and last rightmost digits until the result is a one- or two-digit prime
def is_left_right_truncatable(n):
    while n > 10:
        # Remove the leading leftmost digit
        n = int(str(n)[1:])

        # Remove the last rightmost digit
        n = int(str(n)[:-1])

    return is_prime(n)
