
def all_left_right_truncatable_prime(x):
    # Define a list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x, checking for each number if it is a prime number and if it is left-and-right-truncatable prime number.
    for i in range(1, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_list.append(i)

    # Sort the list of prime numbers in ascending order.
    prime_list.sort()

    # Return the sorted list of prime numbers.
    return prime_list

# Define a function to check if a number is prime or not.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Define a function to check if a number is left-and-right-truncatable prime or not.
def is_left_right_truncatable_prime(n):
    # Check if the number contains any zeros.
    if "0" in str(n):
        return False

    # Check if the number is divisible by 3.
    if n % 3 == 0:
        return False

    # Check if the number is a prime number.
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of the number are simultaneously successively removed down to a one- or two-digit prime number.
    for i in range(1, n + 1):
        if str(n)[i:] == str(n)[i:] and is_prime(int(str(n)[:i] + str(n)[i:])):
            return True

    # If the number is not left-and-right-truncatable prime, return False.
    return False
