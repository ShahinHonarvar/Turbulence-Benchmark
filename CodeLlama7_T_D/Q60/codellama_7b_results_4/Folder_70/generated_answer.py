
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_list = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    lrt_prime_list = []
    # Iterate over the prime numbers in the list
    for p in prime_list:
        # Check if the number is a left-and-right-truncatable prime number
        if is_left_right_truncatable_prime(p):
            # If it is, add it to the list of left-and-right-truncatable prime numbers
            lrt_prime_list.append(p)
    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(lrt_prime_list, reverse=True)
def is_left_right_truncatable_prime(n):
    # Check if the number is a prime number
    if not is_prime(n):
        return False

    # Check if the number contains no 0s
    if "0" in str(n):
        return False

    # Check if the number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(1, len(str(n)))):
        if not is_prime(int(str(n)[:i] + str(n)[i+1:])))]:
            return False

    # If all the checks are successful, the number is a left-and-right-truncatable prime number.
    return True
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False

    return True
