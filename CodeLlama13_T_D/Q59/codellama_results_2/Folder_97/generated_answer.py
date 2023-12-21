
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[645]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    left_truncatable_primes = []
    for p in prime_numbers:
        str_p = str(p)
        if "0" not in str_p and all([is_prime(int(str_p[1:])) for i in range(len(str_p))]):
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes)
