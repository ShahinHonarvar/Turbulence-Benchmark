
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is left- and right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If n is greater than 1, then it is prime
    return True

# Check if a number is left- and right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, then it is not left- and right-truncatable prime number
        return False

    # Check if the leading leftmost digit of n is a prime number
    if not is_prime(int(str(n)[0]))):
        # If the leading leftmost digit of n is not a prime number, then n is not left- and right-truncatable prime number
        return False

    # Check if the last rightmost digit of n is a prime number
    if not is_prime(int(str(n)[-1]))):
        # If the last rightmost digit of n is not a prime number, then n is not left- and right-truncatable prime number
        return False

    # If all the above conditions are satisfied, then n is left- and right-truncatable prime number
    return True
