
def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[78]
    list_of_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            list_of_primes.append(i)
    return sorted(list_of_primes, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False

    for i in range(len(str(n)))):
        if int(str(n)[i:])) != n % 10:
            return False

    return True
