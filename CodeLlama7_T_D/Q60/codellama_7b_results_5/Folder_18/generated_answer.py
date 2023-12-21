
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x
    for i in range(2, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                prime_numbers.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):

            # Check if i divides n
            if n % i == 0:
                return False

    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are both 1 or both 2
    if (str(n)[0] == "1" and str(n)[-1] == "1") or (str(n)[0] == "2" and str(n)[-1] == "2"):
        return False

    # Check if the number can be formed by removing successively the leading leftmost and last rightmost digits of n
    for i in range(len(str(n))) - 1, len(str(n)) - 2, -1:

        # Check if the resulting number is a prime number
        if not is_prime(int(str(n)[i:] + str(n)[:i]))):
            return False

    return True
