
def all_right_truncatable_prime(tup):
    from sympy import isprime
    x = tup[1]
    def check_truncatable(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True
    right_truncatable_primes = [num for num in range(2, x) if check_truncatable(num)]
    return sorted(right_truncatable_primes, reverse=True)
