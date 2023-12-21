 def all_left_right_truncatable_prime(x):
    # Create an empty list to store the results
    result = []
    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the result list
                result.append(i)
    # Return the sorted result list
    return sorted(result)

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Convert n to a string
    s = str(n)

    # Check if the leading leftmost digit of s is 1
    if s[0] != "1":
        # Return False if the leading leftmost digit of s is not 1
        return False

    # Check if the last rightmost digit of s is 1
    if s[-1] != "1":
        # Return False if the last rightmost digit of s is not 1
        return False

    # Iterate from 1 to the length of s - 2 (both inclusive)
    for i in range(1, len(s) - 2 + 1)):
        # Check if the i-th character of s is "0"
        if s[i] == "0":
            # Return False if the i-th character of s is "0"
            return False

    # Return True if all checks are passed
    return True
