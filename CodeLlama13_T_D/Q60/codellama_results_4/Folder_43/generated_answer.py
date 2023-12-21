
def all_left_right_truncatable_prime(tuple_positive_integers):
    left_right_truncatable_primes = []
    for num in range(*tuple_positive_integers):
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(int(len(str(num)) / 2)):
        if str(num)[i] == '0' or not is_prime(num):
            return False
        num = int(str(num)[:-i - 1])
    return is_prime(num)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
