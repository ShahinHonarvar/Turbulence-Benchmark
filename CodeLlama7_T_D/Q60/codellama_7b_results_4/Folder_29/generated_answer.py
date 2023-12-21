
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Loop through the numbers from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_list.append(i)
    return sorted(prime_list, reverse=True)
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n without leaving a remainder
            if n % i == 0:
                # If i divides n without leaving a remainder, return False
                return False

        # If the loop completes without finding any divisors, return True
        return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, return False
        return False

    # Check if the leading leftmost digit of n is 1 or 2
    if str(n)[0] not in ['1', '2']:
        # If the leading leftmost digit of n is not 1 or 2, return False
        return False

    # Check if the last rightmost digit of n is a prime number
    if not is_prime(int(str(n)[-1])), base=10):
        # If the last rightmost digit of n is not a prime number, return False
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime number
    for i in range(1, len(str(n))) - 1):
        # Check if the number is a prime number
        if not is_prime(int(str(n)[i] + str(n)[i+1])), base=10):
            # If the number is not a prime number, return False
            return False

    # If all the checks are successful, return True
    return True
