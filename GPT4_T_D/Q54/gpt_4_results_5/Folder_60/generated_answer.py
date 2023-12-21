
def all_right_truncatable_prime(t):
    from sympy import isprime

    def is_right_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True

    x = t[87]
    truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            truncatable_primes.append(num)

    return sorted(truncatable_primes)
