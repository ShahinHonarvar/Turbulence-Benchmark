
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in ascending order
    prime_numbers.sort()

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Check if a number is prime by dividing it by all the numbers from 2 to the square root of the number
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Check if a number is left-and-right-truncatable prime number by removing the leading leftmost and last rightmost digits until it becomes a one- or two-digit prime
def is_left_right_truncatable_prime(n):
    while len(str(n)) > 1:
        n = int(str(n)[1:])

        if not is_prime(n):
            return False

    return True
