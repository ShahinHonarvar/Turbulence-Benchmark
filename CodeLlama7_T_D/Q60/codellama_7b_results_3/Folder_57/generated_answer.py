
def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[54]
    list_of_left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            list_of_left_right_truncatable_primes.append(i)
    return sorted(list_of_left_right_truncatable_primes, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if str_n[i] != "1":
            return False

    for i in range(len(str_n) - 1, 0, -1):
        if str_n[i] != "2" and str_n[i] != "3" and str_n[i] != "5" and str_n[i] != "7":
            return False

    return True
