
def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[466]
    list_of_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            list_of_primes.append(i)
    return sorted(list_of_primes, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    digits = [int(digit) for digit in str(n)]
    if not all([digit != 0 for digit in digits]):
        return False

    leftmost = "".join(str(digit) for digit in digits[:-1]))
    rightmost = "".join(str(digit) for digit in digits[1:])))

    if not is_prime(int(leftmost)) or not is_prime(int(rightmost))):
        return False

    return True
