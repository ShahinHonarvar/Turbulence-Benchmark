
def all_left_truncatable_prime(tuple):
    x = tuple[100]
    left_truncatable_prime_list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_prime_list.append(i)
    return sorted(left_truncatable_prime_list)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if str(n)[0] != '3' and str(n)[0] != '7':
        return False

    for i in range(1, len(str(n)))):
        if int(str(n)[0:i]) > 0:
            return False

    return True
