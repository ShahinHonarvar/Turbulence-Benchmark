
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i==0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        for _ in range(len(s)):
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True

    x = tup[26]
    primes = [i for i in range(1,x) if is_prime(i)]
    truncatable_primes = [i for i in primes if is_right_truncatable(i)]
    return sorted(truncatable_primes)
