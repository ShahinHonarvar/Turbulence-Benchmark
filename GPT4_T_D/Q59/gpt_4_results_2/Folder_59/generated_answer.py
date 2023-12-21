
def all_left_truncatable_prime(nums):
    import sympy

    def is_prime(n):
        return sympy.isprime(n)

    def left_truncatable_prime(num):
        num = str(num)
        if '0' in num:
            return False
        for i in range(len(num)):
            if not is_prime(int(num[i:])):
                return False
        return True

    def generate_prime(n):
        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes

    x = nums[84]
    primes = generate_prime(x)
    left_truncatable_primes = [i for i in primes if left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)
