
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_list.append(i)
    # sort the list in descending order
    prime_list = sorted(prime_list, reverse=True)
    return prime_list

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    # check if the number contains a zero
    if '0' in str(n):
        return False

    # check if the number is prime after removing its leading leftmost and last rightmost digits
    leading_digits = n % 10
    last_rightmost_digit = n // 10 % 10
    if leading_digits == 0 or last_rightmost_digit == 0:
        return False

    else:

        return is_prime(n % 10) and is_prime(n // 10 % 10))
