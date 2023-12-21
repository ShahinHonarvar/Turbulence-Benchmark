
def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[175]
    list_of_right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            list_of_right_truncatable_primes.append(i)
    return sorted(list_of_right_truncatable_primes)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    string_representation_of_n = str(n)
    for i in range(len(string_representation_of_n) - 1, -1, -1):
        if int(string_representation_of_n[i]) == 0:
            return False

    return True
