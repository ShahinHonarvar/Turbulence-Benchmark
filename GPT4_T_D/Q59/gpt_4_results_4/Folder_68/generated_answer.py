
def all_left_truncatable_prime(tup):
    from sympy import isprime

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = tup[1]
    prime_list = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    prime_list.sort(reverse=True)

    return prime_list
