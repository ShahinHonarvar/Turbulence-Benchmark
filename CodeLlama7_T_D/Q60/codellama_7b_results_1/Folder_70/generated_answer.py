
def all_left_right_truncatable_prime(x):
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
        # Check if the number contains any 0s
        if '0' in str(n):
            return False

        # Check if the number is a prime number
        if not is_prime(n):
            return False

        # Check if the number is left-truncatable prime
        if not is_left_truncatable_prime(n):
            return False

        # Check if the number is right-truncatable prime
        if not is_right_truncatable_prime(n):
            return False

        # If all the above conditions are satisfied, then the number is a left-and-right-truncatable prime number
        return True

    # Define a function to check if a number is left-truncatable prime or not
    def is_left_truncatable_prime(n):
        # Check if the number contains any 0s
        if '0' in str(n):
            return False

        # Check if the number is a prime number
        if not is_prime(n):
            return False

        # Check if the number is left-truncatable prime
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    # Define a function to check if a number is right-truncatable prime or not
    def is_right_truncatable_prime(n):
        # Check if the number contains any 0s
        if '0' in str(n):
            return False

        # Check if the number is a prime number
        if not is_prime(n):
            return False

        # Check if the number is right-truncatable prime
        for i in range(1, int(n ** 0.5) + 1):
            if n % (n - i) == 0:
                return False

        return True

    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    lst = []

    # Iterate through all the numbers less than or equal to x
    for i in range(1, x + 1):
        # Check if the number is a left-and-right-truncatable prime number
        if is_left_right_truncatable_prime(i):
            # If it is, then add it to the list of left-and-right-truncatable prime numbers
            lst.append(i)

    # Return the sorted list of left-and-right-truncatable prime numbers less than or equal to x
    return sorted(lst, reverse=True)
