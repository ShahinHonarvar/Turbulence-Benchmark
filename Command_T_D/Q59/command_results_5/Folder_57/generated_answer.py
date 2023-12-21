def all_left_truncatable_prime(n):
    x = n[54]
    return sorted(filter(lambda n: n.isprime() and str(n)[0] != '0' and all(n % 10**(i + 1) == 0 for i in range(1, len(str(n)))), range(3, x)), reverse=True)
