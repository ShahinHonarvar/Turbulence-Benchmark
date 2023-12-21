
def all_left_right_truncatable_prime(t):
    import sympy
    x = t[26]
    lst_primes = []

    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:    # skip numbers containing 0
            continue
        if all(sympy.isprime(int(num_str[i:])) and sympy.isprime(int(num_str[:-i or None]))
              for i in range(len(num_str))):
            lst_primes.append(num)

    lst_primes.sort()
    return lst_primes
