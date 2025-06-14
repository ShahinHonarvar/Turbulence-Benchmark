 def all_left_right_truncatable_prime(x):
    # Define a list to store the results
    result = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is prime and left-and-right-truncatable prime number
        if is_prime(i) and is_left_right_truncatable_prime(i):
            result.append(i)
    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(result, reverse=True)
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and has no factors other than 1 and itself, it is prime
    return True
def is_left_right_truncatable_prime(n):
    # Check if n is a one- or two-digit prime number
    if n < 10:
        # If n is a one-digit prime number, check if it contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
        return True
    else:
        # If n is a two-digit prime number, check if it contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
        return True
