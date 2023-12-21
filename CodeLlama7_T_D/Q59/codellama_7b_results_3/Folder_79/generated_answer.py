
def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[91]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        num = int(str_n[:i] + str_n[i+1:]))
        if not is_prime(num):
            return False

    return True
