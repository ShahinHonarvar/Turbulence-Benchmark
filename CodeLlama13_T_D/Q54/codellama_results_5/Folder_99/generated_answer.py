
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)

    right_truncatable_primes = []
    for p in prime_numbers:
        str_p = str(p)
        for i in range(len(str_p)):
            if is_prime(int(str_p[:-i])):
                right_truncatable_primes.append(p)
                break
    return sorted(right_truncatable_primes)
