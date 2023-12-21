 def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[92]
    left_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if str(n)[0] == "0":
        return False

    for i in range(2, len(str(n)) - 1):
        if int(str(n)[:i]) != is_prime(int(str(n)[:i])):
            return False

    return True
