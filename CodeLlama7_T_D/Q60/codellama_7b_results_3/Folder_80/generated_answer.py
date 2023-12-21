 def all_left_right_truncatable_prime(x):
    # Create an empty list to store the results
    result = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                result.append(i)
    return sorted(result, reverse=True)
def is_prime(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # Check if n is a multiple of 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, len(str(n)))):
        temp = str(n)[:i] + str(n)[i+1:]
        if not is_prime(int(temp)):
            return False

    return True
