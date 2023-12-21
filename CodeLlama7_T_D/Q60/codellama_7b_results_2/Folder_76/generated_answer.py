 def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    # Filter the list to only include left-and-right-truncatable prime numbers
    filtered_prime_numbers = []
    for prime in prime_numbers:
        if is_left_right_truncatable_prime(prime):
            filtered_prime_numbers.append(prime)
    # Sort the filtered list in descending order
    sorted_filtered_prime_numbers = sorted(filtered_prime_numbers, reverse=True)
    return sorted_filtered_prime_numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    # Check that the number is a prime number
    if not is_prime(n):
        return False

    # Check that the number contains no 0 digits
    if '0' in str(n):
        return False

    # Check that the number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)) - 1, 2, -1):
        if not is_prime(int(str(n)[:i] + str(n)[i+1:]))):
            return False

    return True
