
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x in sorted ascending order. If no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by 2 to n - 1
        for i in range(2, n):
            if n % i == 0:
                return False

        # If the loop completes successfully, it means that n is a prime number.
        return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(1, len(str(n))) and j in range(len(str(n)) - 1, -1)):
        if not is_prime(int(str(n)[i:] + str(n)[:i]))) and not is_prime(int(str(n)[j:] + str(n)[:j]))):
            return False

    # If the loop completes successfully, it means that n is a left-and-right-truncatable prime number.
    return True
