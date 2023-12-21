
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    # Filter the list to only include left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = []
    for prime in prime_numbers:
        if is_left_right_truncatable_prime(prime):
            left_right_truncatable_prime_numbers.append(prime)
    # Sort the list in ascending order
    sorted_list = sorted(left_right_truncatable_prime_numbers)
    return sorted_list

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):

    if not is_prime(n):

        return False

    # Check if the number contains any zeros

    if '0' in str(n):

        return False

    # Remove the leading leftmost digit

    leading_digit = int(str(n)[1:])

    # Check if the number is still prime after removing the leading leftmost digit

    if not is_prime(leading_digit):

        return False

    # Remove the last rightmost digit

    last_rightmost_digit = int(str(n)[:-1])

    # Check if the number is still prime after removing the last rightmost digit

    if not is_prime(last_rightmost_digit):

        return False

    return True
