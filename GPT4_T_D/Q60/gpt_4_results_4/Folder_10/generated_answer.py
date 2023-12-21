
def all_left_right_truncatable_prime(tup):
    from sympy import isprime

    def check_truncatable(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
            if not isprime(int(num_str[:len(num_str) - i])):
                return False
        return True

    x = tup[38]
    truncatable_primes = [num for num in range(11, x + 1) if check_truncatable(num)]
    return sorted(truncatable_primes, reverse=True)
