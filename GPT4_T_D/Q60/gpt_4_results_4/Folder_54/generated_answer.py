
def all_left_right_truncatable_prime(t):
    from sympy import isprime

    def left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
            if not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True

    x = t[88]
    primes = []
    for i in range(2, x+1):
        if left_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)
