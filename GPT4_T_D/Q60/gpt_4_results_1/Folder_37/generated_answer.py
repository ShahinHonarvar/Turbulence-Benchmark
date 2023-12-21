
def all_left_right_truncatable_prime(input_tuple):
    from sympy import isprime

    def truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        else:
            for i in range(len(str_n)):
                if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n)-i])):
                    return False
            return True

    x = input_tuple[35]
    trunc_primes = [i for i in range(x + 1) if truncatable(i)]
    trunc_primes.sort(reverse=True)
    return trunc_primes
