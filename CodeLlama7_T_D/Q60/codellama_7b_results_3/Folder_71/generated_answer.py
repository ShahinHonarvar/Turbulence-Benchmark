
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if the leading leftmost and last rightmost digits of i are simultaneously successively removed down to a one- or two-digit prime.
            if is_left_right_truncatable_prime(i):
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n (inclusive)
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                return False

    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(1, 3):
        # Remove the i-th digit from the left side of n (i.e., the i-th digit from the leftmost end of n)
        l_n = int(str(n)[i:] + str(n)[:i]))
        # Check if l_n is a prime number
        if not is_prime(l_n):
            return False

    for i in range(1, 3):
        # Remove the i-th digit from the right side of n (i.e., the i-th digit from the last rightmost end of n)
        r_n = int(str(n)[:-i] + str(n)[-i:]))
        # Check if r_n is a prime number
        if not is_prime(r_n):
            return False

    return True
