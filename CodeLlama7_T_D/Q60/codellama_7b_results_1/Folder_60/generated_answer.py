
def all_left_right_truncatable_prime(tuple):
    x = tuple[87]
    # Define a function to check if a number is prime or not
    def is_prime(n):
        if n == 1 or n == 0:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    # Define a function to check if a number is left-and-right-truncatable prime or not
    def is_left_right_truncatable_prime(n):
        if n == 1 or n == 0:
            return False

        # Check if the number contains any 0
        if '0' in str(n):
            return False

        # Remove the leading leftmost and last rightmost digits from the number
        leading_leftmost = int(str(n)[1:] or 1)
        last_rightmost = int(str(n)[:-1] or 1))
        # If any of the removed digits is not a prime, return False
        if not is_prime(leading_leftmost) or not is_prime(last_rightmost):
            return False

        return True

    # Initialize an empty list to store all left-and-right-truncatable prime numbers less than or equal to x
    result = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime and is left-and-right-truncatable prime
        if is_prime(i) and is_left_right_truncatable_prime(i):
            result.append(i)

    # Sort the list in ascending order
    result.sort()

    return result
