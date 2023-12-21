
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if n contains any 0s
    for i in range(len(str(n)))):
        if str(n)[i] == "0":
            return False

    # Check if the number can be divided by 3 without leaving a remainder
    if not (n % 3 == 0 and is_prime(int(n / 3)))):
        return False

    # If none of the above conditions are met, then n is a left-and-right-truncatable prime number
    return True
