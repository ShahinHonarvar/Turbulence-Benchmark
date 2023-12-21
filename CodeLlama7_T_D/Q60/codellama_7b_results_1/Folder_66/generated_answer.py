 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []
    # Iterate from 2 to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the result list
                result.append(i)
    # Sort the result list in descending order
    result.sort(reverse=True)
    return result

def is_prime(n):

    # Check if n is a perfect square

    root = int(sqrt(n))
    if root ** 2 == n:
        # If it is a perfect square, check if its last two digits are 01

        if str(root)[-2:] == '01':
            # If the last two digits are 01, return True

            return True

    # If it is not a perfect square or its last two digits are not 01, return False

    return False

def is_left_right_truncatable_prime(n):

    # Check if n is a prime number

    if not is_prime(n):
        # If n is not a prime number, return False

        return False

    # Check if n contains any 0 digits

    for i in str(n):
        if i == '0':
            # If n contains any 0 digits, return False

            return False

    # Check if the leading leftmost digit of n is not 1

    if int(str(n)[0]) != 1:
        # If the leading leftmost digit of n is not 1, return False

        return False

    # Check if the last rightmost digit of n is not 1

    if int(str(n)[-1])) != 1:
        # If the last rightmost digit of n is not 1, return False

        return False

    # If all checks pass, return True

    return True
