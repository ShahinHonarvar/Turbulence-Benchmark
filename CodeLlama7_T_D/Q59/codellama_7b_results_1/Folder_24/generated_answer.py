
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Get the integer at index 65 from the tuple
    x = tuple[65]
    # Iterate through all numbers less than x
    for i in range(2, x):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-truncatable prime number
            if is_left_truncatable_prime(i):
                # Add the prime number to the list
                prime_list.append(i)
    # Sort the list in descending order
    prime_list = sorted(prime_list, reverse=True)
    return prime_list

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("Input must be a positive integer")

    # Check if n is an even number
    if n % 2 == 0:
        return False

    # Check if n is a prime number using the Sieve of Eratosthenes algorithm
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("Input must be a positive integer")

    # Convert the number to a string
    s = str(n)

    # Check if the number contains no 0
    if "0" in s:
        return False

    # Check if all resulting numbers are prime when successively removing the leading leftmost digit
    for i in range(1, len(s)):
        # Get the substring of length i starting from the beginning of the string
        substr = s[:i]
        # Convert the substring to an integer
        n_substr = int(substr)

        # Check if the resulting number is a prime number
        if not is_prime(n_substr):
            return False

    return True
