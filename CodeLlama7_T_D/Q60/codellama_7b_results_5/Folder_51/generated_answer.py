 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the results list
                results.append(i)
    # Return the sorted results list
    return sorted(results)

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if a prime factor is found
                return False

    # If n is a prime number, return True
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Get the digits of n in reverse order
    digits = list(str(n))[::-1]

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(len(digits)):
        # Check if the number formed by removing the leading leftmost digit is a prime number
        if not is_prime(int(''.join(digits[1:]))))):
            # Return False if the leading leftmost digit cannot be removed without creating a non-prime number
            return False

        # Check if the number formed by removing the last rightmost digit is a prime number
        if not is_prime(int(''.join(digits[:-1]))))):
            # Return False if the last rightmost digit cannot be removed without creating a non-prime number
            return False

    # If all checks are passed, return True
    return True
