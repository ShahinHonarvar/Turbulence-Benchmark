
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If n is not divisible by 2 to n - 1, it is prime
    return True

def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0s
    if '0' in str(n):
        return False

    # Check if the number is not a one- or two-digit prime number
    if len(str(n)) == 1 or len(str(n)) == 2:
        if not is_prime(n):
            return False

    # Check if the number is left-truncatable prime number
    for i in range(len(str(n)))):
        if not is_prime(int(str(n)[0:i]))) and int(str(n)[0:i])) <= 1:
            return False

    # Check if the number is right-truncatable prime number
    for i in range(len(str(n)) - 1)):
        if not is_prime(int(str(n)[i + 1:]))) and int(str(n)[i + 1:]))) <= 1:
            return False

    # If the number is left-and-right-truncatable prime number, it is prime
    return True
